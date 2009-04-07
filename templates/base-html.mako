<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<%
import uri

def css_link(file, **kwargs):
  return uri.Static.css_link(file, **kwargs)
%>

<%def name="includes()">
  ${css_link("blueprint/screen.css", media="screen, projection") | n}
  ${css_link("blueprint/print.css", media="print") | n}
  <!--[if IE]
    ${css_link("blueprint/ie.css", media="screen, projection")}
  <![endif]-->
  ${css_link("blueprint/fancy-type.css", media="screen, projection") | n}
  ${next.includes()}
</%def>

<%def name="pager(base_url, url, start, end, prev, next, total)">
  % if prev:
    <a href="${url % prev}">prev</a> &nbsp;|&nbsp;
  % elif prev == 0:
	<a href="${base_url}">prev</a> &nbsp;|&nbsp;
  % endif>
  ${start} - ${end} of ${total}
  % if next:
    &nbsp;|&nbsp; <a href="${url % next}">next</a>
  % endif
</%def>


<html>
  <head>
	<title>${next.title()}</title>
	${includes()}
  </head>
  <body>
	${next.body()}
  </body>
</html>
