#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Futures
from __future__ import unicode_literals
#from __future__ import unicode_literals
#from __future__ import print_function

# Generic/Built-in
import datetime
import argparse

# Other Libs
import onedrivesdk

# Owned


__author__ = "Philipp Germann"
__copyright__ = "Copyright 2017, The Nostalgic project"
__credits__ = ["Andrei Rukavina"]
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Andrei Rukavina"
__email__ = "rukavina.andrei@gmail.com"
__status__ = "Dev"



import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from PIL import Image
import os

input = getattr(__builtins__, 'raw_input', input)

def main():

    #client = onedrivesdk.get_default_client(client_id='c8e4b648-3fc8-4948-8c59-0b14d8972582',
    #                                        scopes=['Files.ReadWrite.All	'])
    #auth_url = client.auth_provider.get_auth_url(redirect_uri)

    redirect_uri = 'http://localhost:5000/login/authorized'
    client_secret = 'twWW+gjygKAXGB43744|*('
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    client = onedrivesdk.get_default_client(
        client_id='c8e4b648-3fc8-4948-8c59-0b14d8972582', scopes=scopes)

    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    #returned_item = client.item(drive='me', id='root').children['newfile.txt'].upload('./path_to_file.txt')

def onedrive_test():
    redirect_uri = "http://localhost:8080/"
    client_secret = "BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM"

    client = onedrivesdk.get_default_client(client_id='00000000481695BB',
                                            scopes=['wl.signin',
                                                    'wl.offline_access',
                                                    'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    # Finally, authenticate!
    client.auth_provider.authenticate(code, redirect_uri, client_secret)

if __name__ == "__main__":
    main()