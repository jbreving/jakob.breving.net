#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jakob Breving'
SITENAME = 'Breving.net'
SITEURL = 'www.breving.net'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('--SIGNAL BOOST--', '#'),
         ('Intelligame', 'https://intelligame.us/'),
         ('--COMICS--', '#'),
         ('Schlock Mercenary', 'https://www.schlockmercenary.com/archives/'),
         ('Erfworld', 'https://archives.erfworld.com/'),
         ('--AUTHORS--', '#'),
         ('Jim Butcher', 'https://www.jim-butcher.com/'),
         ('Brandon Sanderson', 'https://www.brandonsanderson.com/'),
         ('--PODCASTS--', '#'),
         ('Tilt Parenting', 'https://tiltparenting.com/podcast/'),
         ('Up First', 'https://www.npr.org/podcasts/510318/up-first'),
         ('Short Wave', 'https://www.npr.org/podcasts/510351/short-wave'),
         ('The Indicator', 'https://www.npr.org/podcasts/510325/the-indicator-from-planet-money'),
         ('Wow in the World', 'https://www.npr.org/podcasts/510321/wow-in-the-world'),
         ('Talk Python To Me', 'https://talkpython.fm/'),
         ('Python Bytes', 'https://pythonbytes.fm/'),
         ('--OTHER SITES--', '#'),
         ('Python.org', 'http://python.org/'),
         ('Real Python', 'https://realpython.com/'),
         ('linode','https://www.linode.com/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Jakob Breving-Johnson@Pluralsight', 'https://app.pluralsight.com/profile/jakob-breving-johnso'),
          ('jbreving@LinkedIn', 'https://www.linkedin.com/in/jbreving/'),
          ('jbreving@GitHub', 'https://github.com/jbreving'),
          ('jbreving@StackOverflow', 'https://stackoverflow.com/users/8565388/jbreving'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True