#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import urllib2
import json
import sys

parser = OptionParser()
parser.add_option(
    '-b', '--bearer',
    dest='bearer',
    type='string',
    help='OAuth2 Bearer Token'
    )
parser.add_option(
    '-f', '--file_id',
    dest='file_id',
    type='string',
    help='File ID(which is located in script URL)',
    )

def export_script(bearer, file_id):
    api_base = 'https://script.google.com/feeds/download/export'
    url = '%s?id=%s&format=json' % (api_base, file_id)
    header = {
        'Authorization': 'Bearer ' + bearer
    }
    try:
        request = urllib2.Request(url, None, header)
        response = urllib2.urlopen(request)
        body = response.read()
    except urllib2.HTTPError as err:
        raise err

    return body

if __name__ == '__main__':
    (options, args) = parser.parse_args()
    if not (options.bearer and options.file_id):
        parser.print_help()
        sys.exit(0)
    print export_script(options.bearer, options.file_id)
