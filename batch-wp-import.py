import codecs
import datetime
import subprocess

import html2text

from batch import Batch
from model import Post, meta

#"ID","post_author","post_date","post_date_gmt","post_content","post_title","post_category","post_excerpt","post_status","comment_status","ping_status","post_password","post_name","to_ping","pinged","post_modified","post_modified_gmt","post_content_filtered","post_parent","guid","menu_order","post_type","post_mime_type","comment_count"

def strip_accents(string):
  import unicodedata
  return unicodedata.normalize('NFKD', unicode(string)).encode('ASCII', 'ignore')

class ImportPosts(Batch):
	def arguments(self):
		self.opt_parser.add_option("-f", "--file", dest="file", default=None)

	def run(self):
		if not self.options.file:
			raise Exception("Need a file to load from!")

		import_file = open(self.options.file)

		first = True
		for line in import_file:
			_, _, date, _, content, title, _, _, _, _, _, _, name, _, _, modified, _, _, _, _, _, _, _, _ = line.split("\",\"")
			if not name or name == "post_name": continue

			time_created = None
			time_modified = None
			if date:
				time_created = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
			if modified:
				time_modified = datetime.datetime.strptime(modified, "%Y-%m-%d %H:%M:%S")

			content_filename = "blog-posts/%s-%s" % (time_created.strftime("%Y-%m-%d"), name)
			print title, name, content_filename

			with open(content_filename, "w") as blog_content_file:
				blog_content_file.write(content)

			subprocess.check_call(['dos2unix', content_filename])

			blog_content_file = codecs.open(content_filename, "r", "utf-8")
			unix_content = strip_accents(blog_content_file.read())
			blog_content_file.close()

			unix_content = unix_content.replace("\\t", "")
			unix_content = unix_content.replace("\\n", "<br />")

			markdown_content = html2text.html2text(unix_content)
				
			with open(content_filename, "w") as blog_content_file:
				blog_content_file.write(markdown_content)

			post = Post(title, name, name=name, time_created=time_created, time_modified=time_modified)
			meta.session.add(post)
			meta.session.commit()

if __name__ == "__main__":
	batch = ImportPosts()
	batch.start()
