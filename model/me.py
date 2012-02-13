import tornado.web

class Me(object):

    title = 'About Me'
    icon = 'images/me.jpg'
    url = '/'
    content = """I'm a recent Berkeley grad working at Yelp. In the computer world I'm most excited by machine learning and natural language processing (especially of the bayesian and unsupervised variety), low-level performance tricks, and cool hacks.<br/>
                 In the real world, I love to cook and travel.<br/>
                 I'm happily employed, but here's my <a href="/resume/blog">resume</a>, just in case."""
