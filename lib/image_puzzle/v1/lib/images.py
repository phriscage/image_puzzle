import random
import urllib2
import httplib

class NoRedirection(urllib2.HTTPErrorProcessor):
    """ NoRedirection class to catch any 302 """

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        return response

    https_response = http_response


class Images(object):
    """ Images class that pulls from data source and returns a random """

    def __init__(self):
        """ instatiate the class """
        self._url = None
        self._base_url = "http://openphoto.net/volumes/sizes/mike/%i/5.jpg"
        self._random_start = 8000
        self._random_end = 10000
        self._image_urls = []

    def _get_random_url(self):
        """ return a random url """
        return self._base_url % random.randrange(self._random_start, 
            self._random_end)

    def get_image_urls(self):
        """ get a list of valid image urls using a randomly generated
        self._base_url """
        while True:
            image_url = self._get_random_url()
            request = urllib2.Request(image_url)
            opener = urllib2.build_opener(NoRedirection)
            try:
                response = opener.open(request)
                code = response.code
            except urllib2.HTTPError as error:
                print "error"
                code = error.code
            print code
            if code == 200:
                print "Found a successful url!"
                self._image_urls.append(image_url)
            if len(self._image_urls) > 100:
                break
        return self._image_urls


def main():
    """ run the main logic """
    images = Images()
    print images.get_image_urls()

if __name__ == '__main__':
    main()

