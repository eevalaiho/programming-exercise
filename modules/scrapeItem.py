from datetime import datetime


class scrapeItem:
    """
    Class to store the scaping results
    """
    def __init__(self, url, status, pattern, matches):
        self.time = datetime.now()
        self.url = url
        self.status = status
        self.pattern = pattern
        self.matches = matches


    def __str__(self):
        return "%s: %s, %s, %s, matches: %s" % (self.time, self.url, self.status, self.pattern, len(self.matches))
