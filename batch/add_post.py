import datetime
import markdown
import os
import stat

from batch import Batch
from model import Post, meta

class AddPost(Batch):
	def arguments(self):
		self.opt_parser.add_option("-f", "--file", dest="file", default=None)

	def run(self):
		if not self.options.file:
			raise Exception("Missing an argument")

		print "File name:", self.options.file

		existing = Post.by_file(self.options.file)
		if existing:
			content = open(self.options.file).read()

			# validate that it's markdown
			md = markdown.Markdown(extensions=['meta', 'codehilite'])
			md.convert(content)

			existing.markdown_content = content

			st = os.stat(self.options.file)
			existing.time_modified = datetime.datetime.fromtimestamp(st[stat.ST_MTIME])

			meta.session.add(existing)
			meta.session.commit()

			print "updated blog post %s" % existing
		else:
			post = Post(self.options.file)
			meta.session.add(post)
			meta.session.commit()

			print "Added blog post %s" % meta.session.query(Post).filter(Post.id == post.id).all()

if __name__ == "__main__":
	batch = AddPost()
	batch.start()
