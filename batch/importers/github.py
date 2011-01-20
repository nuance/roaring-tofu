import cjson
import datetime
import logging
import urllib2

from batch import Batch
import config
from model import Commit, meta

log = logging.getLogger('import.github')

class GitHub(object):
	@classmethod
	def load_user(cls, user_name):
		user_info = cjson.decode(urllib2.urlopen("http://github.com/api/v1/json/%s" % user_name).read())['user']
		user_name = user_info['name']
		user_projects = [repo['name'] for repo in user_info['repositories'] if not repo['fork']]

		return user_projects, user_name

	@classmethod
	def load_commits(cls, user_name, project):
		try:
			commits = cjson.decode(urllib2.urlopen("http://github.com/api/v2/json/commits/list/%s/%s/master" % (user_name, project)).read())['commits']
		except Exception, e:
			log.exception('Exception loading commits for %s @ %s' % (user_name, project))
			return []

		return commits


class ImportCommits(Batch):
	def arguments(self):
		self.opt_parser.add_option("-u", "--user", dest="user", default=config.github_user)
		self.opt_parser.add_option("-c", "--count", dest="count", default=100)

	def run(self):
		if not self.options.user:
			raise Exception("Need a user to load from!")

		commits = Commit.all_hashes()
		projects, name = GitHub.load_user(self.options.user)
		added = []

		for project in projects:
			new_commits = []
			for commit in GitHub.load_commits(self.options.user, project):
				if commit['id'] not in commits and commit['author']['name'] == name:
					new_commits.append(commit)
			added.extend(new_commits)

			for raw_commit in new_commits:
				author_time = datetime.datetime.strptime(raw_commit['authored_date'][:-6], "%Y-%m-%dT%H:%M:%S")

				offset_hours = int(raw_commit['authored_date'][-6:-3])
				offset_minutes = int(raw_commit['authored_date'][-2:-1])
				if offset_hours < 0: offset_minutes = -offset_minutes
				offset = datetime.timedelta(seconds=(offset_hours * 60 + offset_minutes) * 60)

				commit = Commit(raw_commit['id'], project, raw_commit['message'],
								'http://github.com/%s' % raw_commit['url'], author_time + offset)

				meta.session.add(commit)

		meta.session.commit()
		if added:
			self.log.info("Imported %d new commits" % len(added))

if __name__ == "__main__":
	batch = ImportCommits()
	batch.start()
