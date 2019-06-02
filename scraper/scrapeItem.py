from datetime import datetime


class scrapeItem:
    """
    Class to store the scaping results
    """
    def __init__(self, url, pattern, matches):
        self.time = str(datetime.now())
        self.url = url
        self.pattern = pattern
        self.matches = matches

    def __dict__(self):
        return {
            'time': self.time,
            'url': self.url,
            'pattern': self.pattern,
            'matches': str(self.matches)
        }

    def __str__(self):
        return "%s: %s, %s, matches: %s" % (self.time, self.url, self.pattern, len(self.matches))
