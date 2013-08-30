""" 
    Images file containst the Images class for storing list of urls and
    generating a random url.
"""
import os
import random
import urllib2

class NoRedirection(urllib2.HTTPErrorProcessor):
    """ NoRedirection class to catch any 302 """

    def __init__(self):
        """ instantiate the class """
        pass 

    def http_response(self, request, response):
        """ override http_response method """
        code, msg, hdrs = response.code, response.msg, response.info()
        response.code = code
        response.msg = msg
        response.hdrs = hdrs
        return response

    https_response = http_response


class Images(object):
    """ Images class that has two public methods. Storing a list of random
        image URLs from a specific domain and providing a randomn valid URL.
    """

    def __init__(self):
        """ instantiate the class """
        self._url = None
        self._random_create_start = 8000
        self._random_create_end = 10000
        self._base_url = "http://openphoto.net/volumes/sizes/mike/%s/5.jpg"
        self._image_urls_file_name = "%s/../data/%s" % (os.path.dirname(
            os.path.abspath(__file__)), 'image_urls.txt')
        self._image_urls = []
        self._read_image_urls()


    def _create_random_url(self):
        """ return a random url from the static range """
        return self._base_url % random.randrange(self._random_create_start, 
            self._random_create_end)


    def _read_image_urls(self):
        """ read the image urls from the self._image_urls_file_name and store
        in memory as a list, but return IOError if file DNE or 0 bytes.
        Raise:
            IOError
        """
        if not os.path.isfile(self._image_urls_file_name):
            raise IOError, "'%s' is not found" % self._image_urls_file_name
        if os.path.getsize(self._image_urls_file_name) == 0:
            raise IOError, "'%s' is empty" % self._image_urls_file_name
        for line in open(self._image_urls_file_name, 'r'):
            self._image_urls.append(line.strip())

        
    def create_image_urls(self):
        """ create a list of valid image urls using a randomly generated
        self._base_url and then writes them to a text file.
        """
        self._image_urls = []
        while True:
            image_url = self._create_random_url()
            request = urllib2.Request(image_url)
            opener = urllib2.build_opener(NoRedirection)
            try:
                response = opener.open(request)
                code = response.code
            except urllib2.HTTPError as error:
                code = error.code
            if code == 200:
                print "Found a successful url!"
                self._image_urls.append(image_url)
            if len(self._image_urls) > 100:
                break
        print self._image_urls
        image_url_file = open(self._image_urls_file_name, 'w')
        for image_url in self._image_urls:
            image_url_file.write(image_url + '\n')
        image_url_file.close()


    def get_image(self, image_id):
        """ get a random url from memory and return a url, message """
        index = int(image_id)
        if index >= len(self._image_urls):
            message = "Url index does not exist: '%i'" % index
            return (None, message)
        url = self._image_urls[index]
        message = "Successful URL found."
        return (url, message)
    

    def get_image_random(self):
        """ get a random url from memory and return a url, message """
        index = random.randrange(0, len(self._image_urls_file_name))
        if index >= len(self._image_urls):
            message = "Url index does not exist: '%i'" % index
            return (None, message)
        url = self._image_urls[index]
        message = "Successful URL found."
        return (url, message)
    

    def get_images(self, start=0, limit=100):
        """ return a list of all image urls"""
        if not start:
            start = 0
        if not limit:
            limit = 100
        start = int(start)
        limit = int(limit)
        urls = self._image_urls[start:start + limit]
        message = "%i Successful URLs found." % len(urls)
        return (urls, message)
    

def main():
    """ run the main logic """
    images = Images()
    #print images.create_image_urls()
    print images.get_image_random()
    print images.get_image(12)
    

if __name__ == '__main__':
    main()

