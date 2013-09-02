import urllib2,sys

def get_source(page):
	url=urllib2.urlopen(page)
	source=url.read()
	return source

if __name__ == '__main__':
	data = get_source(sys.argv[1])