#!/usr/bin/env python
# coding: utf-8
"""
    ToolBox.ToolBoxMain
    ~~~~~~~~~~~~~~~~~~~~~~~

    Release date:    __GIT_HEAD_DATE__
    Release version: __GIT_HEAD_REVISION__


"""

__author__ = "Philipp Germann"
__email__ = "-"
__version__ = "__GIT_AUTO_REVISION__"
__date__ = "__GIT_AUTO_DATE__"
__copyright__ = "Copyright 2017-2018, The Nostalgic project"
__maintainer__ = "Philipp Germann"
__credits__ = ["Philipp Germann"]
__license__ = "MPL 2.0"
__status__ = "Dev"

import os
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from lib import config, logger


class OnedriveHandler():
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


def main():
    return 0


if __name__ == '__main__':
    main()