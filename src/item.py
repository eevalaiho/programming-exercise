
class item:
    """
    Class to store the scaping results
    """
    def __init__(self, time, url, pattern, content):
        self.time = time
        self.url = url
        self.pattern = pattern
        self.content = content