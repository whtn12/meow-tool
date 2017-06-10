import sys
import re
import urllib2
import urlparse
import os

ver = "0.9"
currentv = ".".join(map(str, sys.version_info[:3]))
def menu():
	os.system("clear")
	print "[*]--------------------------------------------[*]"
	print "[-] _ _  ___  ___       - URLs finder          [-]"
	print "[-]| | )|___)|   )|   ) - Made By love by:     [-]"
	print "[-]|  / |__  |__/ |/\/  - Jawady Muhammad Habib[-]"
	print "[*]--------------------------------------------[*]"
	
def usage():
	print ""
	print " Usage -> python " + sys.argv[0] + " (option)"
	print " Available options :"
	print " -h || --help                         Display help page"
	print " -up || --update                      Update this tool "
	print " -u=(url) || --url(url)               Fetch urls in this web page"              
	print " -f=(filename) || --fname=(filename)  Fetch urls from webpages located in list"
	print " -v || --version                      Display current version"

def check(url):
	tocrawl = set([url])
	crawled = set([])
	keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
	linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

	while 1:
		try:
			crawling = tocrawl.pop()
			print crawling
		except KeyError:
			raise StopIteration
		url = urlparse.urlparse(crawling)
		try:
			response = urllib2.urlopen(crawling)
		except:
			continue
		msg = response.read()
		startPos = msg.find('<title>')
		if startPos != -1:
			endPos = msg.find('</title>', startPos+7)
			if endPos != -1:
				title = msg[startPos+7:endPos]
				print title
		keywordlist = keywordregex.findall(msg)
		if len(keywordlist) > 0:
			keywordlist = keywordlist[0]
			keywordlist = keywordlist.split(", ")
			print keywordlist
		links = linkregex.findall(msg)
		crawled.add(crawling)
		for link in (links.pop(0) for _ in xrange(len(links))):
			if link.startswith('/'):
				link = 'http://' + url[1] + link
			elif link.startswith('#'):
				link = 'http://' + url[1] + url[2] + link
			elif not link.startswith('http'):
				link = 'http://' + url[1] + '/' + link
			if link not in crawled:
				tocrawl.add(link)


if len(sys.argv)>1:
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		menu()
		usage()
	elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
		menu()
		print "Current version is :" + ver
		print "-> Required version is 2.X"
		print "-> Current  version  is " + currentv 
	elif sys.argv[1] == "-up" or sys.argv[1] == "--update":
		menu()
		#os.system("python update.py")
		print "Feature not yet supported !!"
	else:
		url = sys.argv[1].replace("-u=", "").replace("--url=", "")
		check(url)
		if len(url) == 0:
			fname = sys.argv[2].replace("-f=", "").replace("--fname=", "")
			f = open(fname)
			lines = f.readline()
			for line in lines:
				line = url
				print "> looking up in " + url + " :"
				check(url)
			f.close()
		else:
			menu()
			check(url)	
else:
	menu()
	print "Sorry but there was an error handling your request !!"
	usage()
