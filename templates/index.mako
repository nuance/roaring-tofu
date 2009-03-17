<%inherit file="base-html.mako"/>
<%def name="title()">My blog</%def>

<%def name="includes()">
</%def>

<div class="container">
  <div class="span-8"><h1>The Book of Jones</h1></div>
  <div class="span-10 quiet" style="padding-top:3px;"><h2>Cooking, travel, and techno-babble</h2></div>
  
  <hr class="space"/>

  <div class="span-5 colborder">
    <h6>Recent Tweet</h6>
    <p class="incr small">
      <span class="dquo">&#8220;</span>This is exactly 140 characters, or at least is really should be something close to it- what would it be if I couldn't come up with that many&#8221;
      <a href="foo">link</a>
    </p>
  </div>

  <div class="span-5 colborder">
    <h6>Recent Commits</h6>
    <p class="incr">
      <a href="/">python-nlp</a> - Fix imports - 2/17/09<br/>
      Pushed blah<br/>
    </p>
  </div>

  <div class="span-6 colborder">
    <h6>Recent Reviews</h6>
    <p class="incr">
      <img src="4star.png" alt="4 stars">
      <a href="yelp.com">Gordo</a> - Fix imports - 2/17/09<br/>
      <img src="2star.png" alt="4 stars">
      <a href="yelp.com">Ici</a> - Fix imports - 2/17/09<br/>
    </p>
  </div>

  <div class="span-5 last">
    <h6>Recently Read</h6>
    <p class="incr">
      <span class="span-1">favicon</span>
      Article title <a href="foo">(domain.com)</a>
    </p>
  </div>

  <hr/>
  <hr class="space"/>

  <div class="blog span-18 colborder">
    % for post in posts:
    <div class="post">
      <div class="post-header">
  	    <h2 class="post_title">${post.title}</h2>
  	    <span class="small">
  	      <a href="${uri.Blog.view_post(post.id)}">permalink</a>
  	    </span>
  	    <div class="post_time">Posted ${post.date_created}</div>
      </div>
  	  <p class="post_body">${post.body_html}</p>
  	  % if post.updated:
        <em>Updated: ${post.date_modified}</em>
  	  % endif
  	</div>
    % endfor
  </div>
  
  <div class="rightbar span-5 last">
    <div class="box">
      <h3>About Me</h3><br>
      <img src="picture-of-me"/><br>
      <p>I'm a recent Berkeley grad working at Yelp. In the computer world I'm most excited by machine learning and natural language processing (especially of the bayesian and unsupervised variety), low-level performance tricks, and cool hacks.</p>
      <p>In the real world, I love to cook, travel and I'm getting back into rock climbing.</p>
    </div>
    <hr class="space"/>
    <div class="box">
      Do I want a blog archive thing here? They look kind of ugly
    </div>
  </div>
</div>
