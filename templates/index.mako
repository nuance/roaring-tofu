<%inherit file="base-html.mako"/>
<%def name="title()">My blog</%def>

<%def name="includes()">
<style type="text/css" media="screen, projection">
  img.favicon {height: 8px; width: 8px;}
</style>
</%def>

<%!
from uri import Blog

view_post = lambda post_id: Blog.view_post(post_id)
%>

<div class="container">

  <!-- Header -->
  <div class="span-8"><h1>The Book of Jones</h1></div>
  <div class="span-10 quiet" style="padding-top:3px;"><h2>Cooking, travel, and techno-babble</h2></div>
  <hr class="space"/>

  <!-- Action Boxes -->
  
  <!-- Twitter feed -->
  <div class="span-5 colborder">
    <h6>Recent Tweet</h6>
    <p class="incr small" style="padding-left:8px;">
      <span class="dquo">&#8220;</span>${recent_tweet}&#8221;
      <a href="foo">link</a>
    </p>
  </div>

  <!-- Github commits -->
  <div class="span-5 colborder">
    <h6>Recent Commits</h6>
    <p class="incr">
      % for commit in commits:
        <a href="${commit.url}">${commit.project}</a> - ${commit.message} - ${commit.date}<br/>
      % endfor
    </p>
  </div>

  <!-- Yelp reviews -->
  <div class="span-6 colborder">
    <h6>Recent Reviews</h6>
    <p class="incr">
      % for review in reviews:
        <img src="${review.stars_img}" alt="${review.stars_alt_text}">
        <a href="${review.url}">${review.biz_name}</a> - ${review.snippet} - ${review.date}<br/>
      % endfor
    </p>
  </div>

  <!-- del.icio.us-style article syndication -->
  <div class="span-5 last">
    <h6>Recently Read</h6>
    <p class="incr">
      % for article in articles:
        <span class="span-1"><img src="${article.site_favicon}" alt="${article.site_name}" class="favicon"/></span>
        ${article.title} - <a href="${article.url}">(${article.domain})</a> - ${article.date}<br/>
      % endfor
    </p>
  </div>

  <hr/>
  <hr class="space"/>

  <!-- The blog -->
  <div class="blog span-18 colborder">
    % for post in posts:
      <div class="post">
        <div class="post-header">
    	    <h2 class="post_title">${post.title}</h2>
    	    <span class="small">
    	      <a href="${view_post(post.id)}">permalink</a>
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
  
  <!-- Side bar -->
  <div id="sidebar" class="rightbar span-5 last">
    
    <!-- About me -->
    <div id="aboutme" class="box">
      <h3>About Me</h3><br>
      <img src="picture-of-me"/><br>
      <p>I'm a recent Berkeley grad working at Yelp. In the computer world I'm most excited by machine learning and natural language processing (especially of the bayesian and unsupervised variety), low-level performance tricks, and cool hacks.</p>
      <p>In the real world, I love to cook, travel and I'm getting back into rock climbing.</p>
    </div>
    <hr class="space"/>
    
    <!-- Post Index / Calendar -->
    <div id="blogindex" class="box">
      Do I want a blog archive thing here? They look kind of ugly. A calendar might be kind of slick, though...
    </div>
  </div>
</div>
