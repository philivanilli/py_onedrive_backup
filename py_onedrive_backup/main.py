#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generic/Built-in

import datetime
import argparse
import os

###
# Other Libs
###
import onedrivesdk

from onedrivesdk.helpers import GetAuthCodeServer

###
# Owned
###
__author__ = "Philipp Germann"
__copyright__ = "Copyright 2017, The Nostalgic project"
__credits__ = ["Philipp Germann"]
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Philipp Germann"
__email__ = "-"
__status__ = "Dev"

###
# ToDos
###

#todo 1 implement one time app auth
#   todo 1.1 check if pickle session file exists
#   todo 1.2 check if auth is ok

#todo 2 read/write json/pickle object for app data
#   todo 2.1 pack data to zip and upload to onedrive folder

#todo 3 upload/download data to/from onedrive

#todo 4 zip/unzip data

#todo logging output

input = getattr(__builtins__, 'raw_input', input)

def onedrive_add_folder(client):
    f = onedrivesdk.Folder()
    i = onedrivesdk.Item()
    i.name = 'New Folder'
    i.folder = f
    returned_item = client.item(drive='me', id='root').children.add(i)


def onedrive_auth_own_app_cli():
    redirect_uri = 'http://localhost:5000/login/authorized'
    client_secret = 'bnQV76$%^inqsaDBRKG479#'
    client_id = 'c8e4b648-3fc8-4948-8c59-0b14d8972582'
    api_base_url = 'https://api.onedrive.com/v1.0/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)

    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')

    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    return client


def onedrive_auth_own_app_webserver():
    redirect_uri = 'http://localhost:5000/login/authorized'
    client_secret = 'bnQV76$%^inqsaDBRKG479#'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    client = onedrivesdk.get_default_client(
        client_id='c8e4b648-3fc8-4948-8c59-0b14d8972582',
        scopes=scopes)

    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    client.auth_provider.save_session()

    #onedrive_add_folder(client)

    # returned_item = client.item(drive='me', id='root').children['newfile.txt'].upload('./path_to_file.txt')

def onedrive_example_auth():
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


# def onedrive_load_session():
#     auth_provider = onedrivesdk.AuthProvider(http_provider,
#                                              client_id='c8e4b648-3fc8-4948-8c59-0b14d8972582',
#                                              scopes = ['wl.signin',
#                                                       'wl.offline_access',
#                                                       'onedrive.readwrite']))
#     auth_provider.load_session()
#     auth_provider.refresh_token()
#     client = onedrivesdk.OneDriveClient(base_url, auth_provider, http_provider)


if __name__ == "__main__":
    # if os.path.isfile("session.pickle"):
    #    onedrive_load_session()
    #    onedrive_add_folder

    client = onedrive_auth_own_app_cli()

    onedrive_add_folder(client)
