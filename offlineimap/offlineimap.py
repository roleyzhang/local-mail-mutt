import keyring
import os

with open(os.path.expanduser('~/.localmail-username-gmail'), 'r') as localmail_username_file:
    localmail_username = localmail_username_file.read()

