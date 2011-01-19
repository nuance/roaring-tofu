<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<%
import util.uri
from config import ga_key

css_link = util.uri.Static.css_link
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
  ${start + 1} - ${end} of ${total}
  % if next:
    &nbsp;|&nbsp; <a href="${url % next}">next</a>
  % endif
</%def>

<%def name="google_analytics()">
  <script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
  </script>
  <script type="text/javascript">
    try{
      var pageTracker = _gat._getTracker("UA-${ga_key}");
        pageTracker._trackPageview();
    } catch(err) {}
  </script>
</%def>

<html>
  <head>
	<title>${next.title()}</title>
	${includes()}
  </head>
  <body>
	${next.body()}
	${google_analytics()}
  </body>
</html>
