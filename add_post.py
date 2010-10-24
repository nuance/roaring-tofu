from batch import Batch
from model import Post, meta

class AddPost(Batch):
	def arguments(self):
		self.opt_parser.add_option("-f", "--file", dest="file", default=None)

	def run(self):
		if not self.options.file:
			raise Exception("Missing an argument")

		print "File name:", self.options.file

		post = Post(self.options.file)
		meta.session.add(post)
		meta.session.commit()

		print "Added blog post %s" % meta.session.query(Post).filter(Post.id == post.id).all()

if __name__ == "__main__":
	batch = AddPost()
	batch.start()
