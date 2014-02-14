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
parser.add_option(
    '-s', '--script_id',
    dest='script_id',
    type='string',
    help='Script ID(which is obtained by running gae_export.py)',
    )
parser.add_option(
    '-p', '--script_path',
    dest='script_path',
    type='string',
    help='Script path',
    )

def import_script(bearer, file_id, script_id, fh):
    api_base = 'https://www.googleapis.com/upload/drive/v2/files/'
    url = api_base + file_id
    header = {
        'Content-Type': 'application/vnd.google-apps.script+json',
        'Authorization': 'Bearer ' + bearer
    }

    data = {
      'files': [
        {
          'id': script_id,
          'name': 'Code',
          'type': 'server_js',
          'source': fh.read()
        },
      ]
    }

    try:
        request = urllib2.Request(url, json.dumps(data), header)
        request.get_method = lambda: 'PUT'
        response = urllib2.urlopen(request)
        body = response.read()
    except urllib2.HTTPError as err:
        raise err

    return body

if __name__ == '__main__':
    (options, args) = parser.parse_args()
    if not (options.bearer and options.file_id and options.script_id and options.script_path):
        parser.print_help()
        sys.exit(0)
    with open(options.script_path, 'r') as fh:
        print import_script(options.bearer, options.file_id, options.script_id, fh)
