import click
import owncloud
from owncloud import Client


@click.command()
@click.option("--url", type=str, required=True, help="OwnCloud Instance to use.")
@click.option("--username", type=str, required=True, help="Username to use.")
@click.option("--folder", type=str, required=True, help="Folder of which the content will be shared.")
def oc_share(url: str, username: str, folder: str):
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
    oc_share()
