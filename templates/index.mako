<%inherit file="base-html.mako"/>
<%namespace name="base" file="base-html.mako"/>

<%!
from uri import Blog, Static
import util

view_post = Blog.view_post
css_link = Static.css_link
js_link = Static.js_link
%>

<%def name="title()">My blog</%def>

<%def name="includes()">
  ${css_link("blueprint/tabs.css", media="screen, projection") | n}
  ${css_link("blog.css", media="screen, projection") | n}

  ${js_link("blog.js") | n}
<script>var disqus_developer = true</script>
</%def>


<div class="container">

  <!-- Header -->
  <div class="push-05 span-8 header"><h1>The Book of Jones</h1></div>
  <div class="push-1 span-10 quiet subheader"><h2>Cooking, travel, and techno-babble</h2></div>
  <hr class="thin"/>

  <!-- Action Boxes -->

  <!-- Yelp reviews -->
  <div class="push-05 span-7 colborder first top-box">
    <h6>Recent Reviews</h6>
    <p class="incr">
      % for review in reviews:
	    <a href="${review.url | n}" rel="nofollow">${review.business}</a> -
        <img src="${review.stars_img | n}" alt="${review.rating}/5 stars" class="centered"> -
        ${review.snippet} -
		${util.relative_time(review.time_authored)}<br/>
      % endfor
    </p>
  </div>

  <!-- Github commits -->
  <div class="span-7 colborder top-box">
    <h6>Recent Commits</h6>
    <p class="incr">
      % for commit in commits:
        <a href="${commit.url | n}" rel="nofollow">${commit.project}</a> - ${commit.message} - ${util.relative_time(commit.time_authored)}<br/>
      % endfor
    </p>
  </div>

  <!-- Twitter feed -->
  <div class="span-6 last top-box">
    <h6>Recent Tweet</h6>
    <p class="incr small indent">
      <span class="dquo">&#8220;</span>${recent_tweet.text | util.linkify_tweet}&#8221;<br/>
      - ${util.relative_time(recent_tweet.time_created)}&nbsp;&nbsp;
	  <a href="${recent_tweet.link | n}" rel="nofollow">link</a>
    </p>
  </div>

  <hr style="margin-bottom:0;"/>

  <!-- Tab bar -->
  <div class="tabbar span-20 header">
	<ul class="tabs">
	  <li class="active"><a href="/">Blog</a></li>
	  <li><a href="projects">Projects</a></li>
	</ul>
  </div>

  <hr/>

  <!-- The blog -->
  <div class="blog push-05 span-15 colborder">
	% if len(posts) > 1:
	  <div class="pager">
		${base.pager("/", "/%d", start, end, prev, next, total)}
	  </div>
	% endif

    % for post in posts:
      <div class="post">
        <div class="post-header">
		  <h2 class="post-title">${post.title}</h2>
    	  <span class="small title-permalink">
    	    <a href="${view_post(post.id)}">permalink</a>
    	  </span>
        </div>
    	<div class="post_time">
		  Posted ${post.date_created}
     	  % if post.updated and post.date_created != post.date_modified:
            <em>Updated: ${post.date_modified}</em>
    	  % endif
		</div>
    	<p class="post_body">${post.content | n}</p>

		% if len(posts) == 1:
		  <div id="disqus_thread">
		  </div>
		  <script type="text/javascript" 
				  src="http://disqus.com/forums/thebookofjones/embed.js"></script>
		  <noscript>
			<a href="http://thebookofjones.disqus.com/?url=ref">
			  View the discussion thread.
			</a>
		  </noscript>
		  <a href="http://disqus.com" class="dsq-brlink">
			blog comments powered by <span class="logo-disqus">Disqus</span>
		  </a>
		% else:
		  <a href="${view_post(post.id)}#disqus_thread">View Comments</a>
		% endif
      </div>
    % endfor

	% if len(posts) > 1:
	  <div class="pager">
		${base.pager("/", "/%d", start, end, prev, next, total)}
	  </div>
	% endif

  </div>
  
  <!-- Side bar -->
  <div id="sidebar" class="rightbar span-6 last">
    
    <!-- About me -->
    <div id="aboutme" class="box">
      <h3>About Me</h3>
      <img src="/static/images/me.png"/><br/>
      <p>I'm a recent Berkeley grad working at Yelp. In the computer world I'm most excited by machine learning and natural language processing (especially of the bayesian and unsupervised variety), low-level performance tricks, and cool hacks.</p>
      <p>In the real world, I love to cook, travel and I'm getting back into rock climbing.</p>
    </div>
    <hr class="space"/>

	<!-- del.icio.us-style article syndication -->
	<div id="articles" class="box">
      <h6>Recently Read</h6>
      <p class="incr">
		% for article in articles:
          <span class="span-1"><img src="${article.favicon | n}" alt="${article.domain}" class="favicon"/></span>
          ${article.title} - <a href="${article.url}" rel="nofollow">(${article.domain})</a> - ${util.relative_time(article.time_added)}<br/>
		% endfor
      </p>
	</div>
    <hr class="space"/>
  </div>
</div>

<script type="text/javascript">
//<![CDATA[
(function() {
		var links = document.getElementsByTagName('a');
		var query = '?';
		for(var i = 0; i < links.length; i++) {
			if(links[i].href.indexOf('#disqus_thread') >= 0) {
				query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
			}
		}
		document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/thebookofjones/get_num_replies.js' + query + '"></' + 'script>');
	})();
//]]>
</script>

