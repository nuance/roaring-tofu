<%inherit file="base-html.mako"/>
<%def name="title()">My blog</%def>
<%def name="includes()">
  ${uri.Static.css_link('blog.css')}
</%def>
<div class="blog">
  % for post in posts:
  <div class="post">
    <div class="post-header">
	    <h3 class="title">
	      <a href="${uri.Blog.view_post(post.id)}">
	        ${post.title}
	      </a>
	    </h3>
	    <div class="time">${post.date_created}</div>
    </div>
	  <p class="body">${post.body_html}</p>
	  % if post.updated:
      <em>Updated: ${post.date_modified}</em>
	  % endif
	</div>
  % endfor
</div>
