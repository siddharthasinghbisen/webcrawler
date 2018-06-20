from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)


    def page_links(self):
        return self.links

    def reset(self):
        HTMLParser.reset(self)
        self.extracting = False
        self.links      = []

    def handle_startag(self, tag, attrs):
        if tag == "td" or tag == "a":
            attrs = dict(attrs)   # save us from iterating over the attrs
        if tag == "td" and attrs.get("class", "") == "title":
            self.extracting = True
        elif tag == "a" and "href" in attrs and self.extracting:
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "td":
            self.extracting = False

    def error(self, message):
        pass

