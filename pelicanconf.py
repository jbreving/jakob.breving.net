#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jakob Breving-Johnson'
SITENAME = 'Breving.net'
SITEURL = 'http://www.breving.net'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('--SIGNAL BOOST>>', '#'),
         ('Intelligame', 'https://intelligame.us/'),
         ('<<SIGNAL BOOST--', '#'),
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
         ('', '#'),
         ('--VIDEO ONLINE--', '#'),
         ('Clear Skies - Star Trek Adventures Tabletop RPG', 'https://www.youtube.com/playlist?list=PLHVibqh7yRwogVxLuZzYAlEDkyz0DB0b8'),
         ('Critical Role', 'https://critrole.com/'),
         ('--OTHER SITES--', '#'),
         ('Brent Ozar', 'https://www.brentozar.com/'),
         ('SQL Server First Responder Kit', 'https://github.com/BrentOzarULTD/SQL-Server-First-Responder-Kit'),
         ('sp_whoisactive', 'http://whoisactive.com/'),
         ('Ola Hallengren SQL Server Maintenance Solution', 'https://ola.hallengren.com/'),
         ('Python.org', 'http://python.org/'),
         ('Real Python', 'https://realpython.com/'),
         ('linode','https://www.linode.com/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Pluralsight', 'https://app.pluralsight.com/profile/jakob-breving-johnso'),
          ('LinkedIn', 'https://www.linkedin.com/in/jbreving/'),
          ('GitHub', 'https://github.com/jbreving'),
          ('StackOverflow', 'https://stackoverflow.com/users/8565388/jbreving'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './themes/pelican-blueidea/'