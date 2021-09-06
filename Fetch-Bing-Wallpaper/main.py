
# Reaches out to the bing.com homepage and retrieves the URL for the daily wallpaper
from html.parser import HTMLParser
import urllib
import urllib.request

# Make a definition of HTMLParser and customize the functions
class MyHTMLParser(HTMLParser):
    wallpaper = ""
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag: {} with {} ".format(tag, attrs))
        link = ""
        if(tag == "link"):
            for x in attrs:
                if x == ("id", "preloadBg"):
                    for y in attrs:
                        if y[0] == "href":
                            self.wallpaper = (y[1])

#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

#    def handle_data(self, data):
#        print("Encountered some data  :", data)

def get_wall():
    localSite = "index.html"
    remoteSite = "http://www.bing.com"
    bLocalHtml = False
    parser = MyHTMLParser()

    if(bLocalHtml):
        rawhtml = open(localSite, "r", encoding="utf-8")
        parser.feed(rawhtml.read())
    else:
        data = urllib.request.urlopen(remoteSite)
        parser.feed(data.read().decode('utf-8'))

    print(remoteSite + parser.wallpaper)

if __name__ == '__main__':
    get_wall()

