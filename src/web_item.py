from datetime import datetime


class web_item:
    """
    Class to store the scaping results
    """
    def __init__(self, url, pattern, content):
        self.time = str(datetime.now())
        self.url = url
        self.pattern = pattern
        self.content = content