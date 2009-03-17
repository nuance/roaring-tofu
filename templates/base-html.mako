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

<html>
  <head>
	<title>${next.title()}</title>
	${includes()}
  </head>
  <body>
	${next.body()}
  </body>
</html>
