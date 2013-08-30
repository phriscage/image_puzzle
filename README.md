Image Puzzle
================================

A basic Python flask application generating a random image url from openphoto.net.

There isn't a need for Sphinx docs yet, since there is only one method. 


Quick Start
-------------------------

Execute main.py to launch the app.

    $ ./lib/main.py
    * Running on http://0.0.0.0:8000/
    * Restarting with reloader

Call the versioned images URL to generate a random URL.

    $ wget -O - http://0.0.0.0:8000/api/v1/images
    --2013-08-30 03:58:03--  http://0.0.0.0:8000/api/v1/images
    Connecting to 0.0.0.0:8000... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 124 [application/json]
    Saving to: “STDOUT”

     0% [                                                 ] 0           --.-K/s              {
      "url": "http://openphoto.net/volumes/sizes/mike/8417/5.jpg",
      "message": "Successful URL found.",
      "success": true
    100%[================================================>] 124         --.-K/s   in 0s

    2013-08-30 03:58:03 (22.7 MB/s) - written to stdout [124/124]


TODO
-------------------------

Create configuration file.
Create Ant build file for RPM.
Create Sphinx docs when additional methods are added.
