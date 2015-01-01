#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mike Panciera'
SITENAME = u'Mike Panciera'
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
LINKS = (('Justin Duke', 'http://jmduke.com/' ), )

# Social widget
SOCIAL = (
    ('LinkedIn', 'http://www.linkedin.com/pub/mike-panciera/39/938/a52' ),
    ('GitHub', 'https://github.com/averagehat' ), 
    )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#Set to true fixes the ".html" hrefs in one of the posts. possibly SITEURL is not set correctly?
# https://github.com/getpelican/pelican/issues/1526
#RELATIVE_URLS = False

# for ipynb plugin (from https://github.com/danielfrg/pelican-ipynb)

MARKUP = ('md', 'ipynb')
PLUGINS = ['ipynb']
PLUGIN_PATH = './plugins'
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = { 'extra/favicon.ico': {'path': 'favicon.ico'} }
