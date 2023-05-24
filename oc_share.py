import owncloud
import typer
from owncloud import Client
from rich.progress import track


def oc_share(
        url: str,
        username: str,
        folder: str,
        password: str = typer.Option(..., prompt=True, hide_input=True)
):
    oc = owncloud.Client(url)
    oc.login(username, password)
    share_all_in_folder(oc, folder)


def share_all_in_folder(oc: Client, folder: str):
    """Share all files in a given folder"""
    for item in track(oc.list(folder), description="Creating links..."):
        link_info = oc.share_file_with_link(item)
        print(f"{link_info.get_path()}: {link_info.get_link()}")


if __name__ == '__main__':
    typer.run(oc_share)
