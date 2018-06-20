from html.parser import HTMLParser

class LinkExctractor(HTMLParser):

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