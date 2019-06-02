from datetime import datetime


class ScrapeItem:
    """
    Class to store the scaping results
    """
    def __init__(self, url, pattern, content):
        self.time = str(datetime.now())
        self.url = url
        self.pattern = pattern
        self.content = content

    def __str__(self):
        return "%s: %s, %s, %s" % (self.time, self.url, self.pattern, self.content)
