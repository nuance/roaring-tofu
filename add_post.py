from batch import Batch
from model import Post, meta

class AddPost(Batch):
	def arguments(self):
		self.opt_parser.add_option("-t", "--title", dest="title", default=None)
		self.opt_parser.add_option("-f", "--file", dest="file", default=None)

	def run(self):
		if not self.options.title or not self.options.file:
			raise Exception("Missing an argument")

		print "Title:", self.options.title
		print "File name:", self.options.file

		post = Post(self.options.title, self.options.file)
		meta.session.add(post)
		meta.session.commit()

if __name__ == "__main__":
	batch = AddPost()
	batch.start()
