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
        self._base_url = "http://openphoto.net/volumes/sizes/mike/%i/5.jpg"
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
        in memory as a list, but return False if file DNE.
        Returns:
            True/False
        """
        if not os.path.isfile(self._image_urls_file_name):
            return False
        for line in open(self._image_urls_file_name, 'r'):
            self._image_urls.append(line.strip())
        return True

        
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


    def read(self):
        """ get a random url from memory and return in a dictionary """
        if not self._image_urls:
            if not self._read_image_urls():
                message = ("File does not exist: '%s'" 
                    % self._image_urls_file_name)
                return { 'message': message, 'success': False, 'url': None }
        index = random.randrange(0, len(self._image_urls_file_name))
        if index >= len(self._image_urls):
            message = "Url index does not exist: '%i'" % index
            return { 'message': message, 'success': False, 'url': None }
        url = self._image_urls[index]
        message = "Successful URL found."
        return { 'message': message, 'success': True, 'url': url }
    

def main():
    """ run the main logic """
    images = Images()
    print images.create_image_urls()
    #print images.read()
    

if __name__ == '__main__':
    main()

