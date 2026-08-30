class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.counter += 1
        code = str(self.counter)
        self.url_map[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl.split('/')[-1]
        return self.url_map[code]


