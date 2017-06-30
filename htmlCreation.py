document_name = input('What do you want the document name to be?: ')
file_name = "{0}{1}".format(document_name, ".html")

INITIAL_HTML_TAGS = '<!doctype html><html><head><meta charset="utf-8">'

TITLE = '<title>{0}</title>'.format("starting text".lower().title())
KEYWORDS = '<meta name="keywords" content="{0}" />'.format("Starting, Text")
DESCRIPTION = '<meta name="description" content="{0}" />'.format("starting text".capitalize())
JQUERY_LINK = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js'
JQUERY_LINK_TAG = '<script src="{0}"></script>'.format(JQUERY_LINK)
JQUERY_DOCUMENT_READY_FUNCTION ='<script type="text/javascript">$(document).ready(function() {/*SCRIPT HERE*\});</script>'

JAVASCRIPT_YEAR_FUNCTION = '<script>function getCurrentYear() {var d = new Date();\n\Year = d.getFullYear();document.write(Year);</script>'

CLOSINGHEAD_OPENINGBODY_HEADER_NAV = '</head><body><header><!--HEADER GOES HERE--></header><nav><!--NAVIGATION GOES HERE--></nav>'
BODY_CONTENT = '<h1>Starting Text</h1><p> Starting text in sentence </p>'

FOOTER = '<footer>{0} Copyright Matt Hoskins <script type="text/javascript">getCurrentYear();</script>.</footer>'.format("&copy;")

ENDING_HTML_TAGS = '</body></html>'
HTML_PAGE_ELEMENTS = {
	1:INITIAL_HTML_TAGS,
	2:TITLE,
	3:KEYWORDS,
	4:DESCRIPTION,
	5:JQUERY_LINK_TAG,
	6:JQUERY_DOCUMENT_READY_FUNCTION,
	7:JAVASCRIPT_YEAR_FUNCTION,
	8:CLOSINGHEAD_OPENINGBODY_HEADER_NAV,
	9:BODY_CONTENT,
	10:FOOTER,
	11:ENDING_HTML_TAGS
	}

created_file=open(file_name, "w")#PUT ALL DATA TO HTML PAGE

for key,value in HTML_PAGE_ELEMENTS.items():
	created_file.write(value)


created_file.close()#CLOSE IT DOWN

print("File Created")
#print(HTML_ELEMENTS["start"])
