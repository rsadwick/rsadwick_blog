#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan Sadwick'
SITENAME = "ryan's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
BIBLE_VERSES = (('Now glory be to God!  By his mighty power at work within usm he is able to accomplish infinitely more than we should ever dare to ask or hope.', 'Ephesians 3:20'),
          ("Follow only what is good.  Remember that those who do good prove that they are God's children, and those who do evil prove that they do not know God.", '3 John 11'),
          ("God has given gifts to each of you from his great variety of spiritual gifts.  Manage them well so that God's generosity can flow through you.", "1 Peter 4:10"),
          ("So let us come boldly to the throne of our gracious God.  There we will receive his mercy, and we will find grace to help us when we need it.", "Hebrews 4:16"),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ASSET_DEBUG = True
