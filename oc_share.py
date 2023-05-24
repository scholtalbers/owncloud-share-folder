import argparse

import click
import owncloud
from owncloud import Client


def oc_share(url: str, username: str, folder: str):
    # could be replaced by getpass()
    password = click.termui.prompt(f"Password for {username}", hide_input=True)
    oc = owncloud.Client(url)
    oc.login(username, password)
    share_all_in_folder(oc, folder)


def share_all_in_folder(oc: Client, folder: str):
    """Share all files in a given folder"""
    for item in oc.list(folder):
        link_info = oc.share_file_with_link(item)
        print(f"{link_info.get_path()}: {link_info.get_link()}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Share a OwnCloud directory")
    parser.add_argument("--url", dest="url", required=True, help="OwnCloud Instance to use.")
    parser.add_argument("--username", dest="username", required=True, help="Username to use.")
    parser.add_argument("--folder", dest="folder", required=True, help="Folder of which the content will be shared.")

    args = parser.parse_args()
    oc_share(args.url, args.username, args.folder)
