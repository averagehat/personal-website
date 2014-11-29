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
#RELATIVE_URLS = True


# for ipynb plugin (from https://github.com/danielfrg/pelican-ipynb)
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']



