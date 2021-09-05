
#!/usr/bin/python3

# Reaches out to the bing.com homepage and retrieves the URL for the daily wallpaper
from html.parser import HTMLParser
import urllib
import urllib.request
from urllib.request import Request, urlopen

# Make a definition of HTMLParser and customize the functions
class MyHTMLParser(HTMLParser):
	wallpaper = ""
	sentence_found = False

	def handle_starttag(self, tag, attrs):
		
		# print("Encountered a start tag: {} with {} ".format(tag, attrs))
		link = ""
		#print(f"{tag} : {attrs}")
		if(tag == "div"):
			for x in attrs:
				if x == ("id", "random_word"):
		 			self.sentence_found = True

#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

	def handle_data(self, data):
		if(self.sentence_found == True):
			print(data)
			self.sentence_found = False

def get_wall():
	localSite = "index.html"
	remoteSite = "https://randomword.com/sentence"
	bLocalHtml = False
	parser = MyHTMLParser()

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	   'Accept-Encoding': 'none',
	   'Accept-Language': 'en-US,en;q=0.8',
	   'Connection': 'keep-alive'}

	#req = Request(remoteSite, headers={'User-Agent': 'Mozilla/5.0'})
	req = Request(remoteSite, headers=hdr)
	if(bLocalHtml):
		rawhtml = open(localSite, "r", encoding="utf-8")
		parser.feed(rawhtml.read())
	else:
		data = urllib.request.urlopen(req)
		parser.feed(data.read().decode('utf-8'))

	#print(remoteSite + parser.wallpaper)

if __name__ == '__main__':
	get_wall()

