# Share OwnCloud content

A quick script to generate public links for any given OwnCloud folder.

## Quick Start

```
pip install click pyocclient
python oc_share.py --url <owncloud instance> --username <username> --folder </a/owncloud/folder>

# output:
/a/owncloud/folder/file1.txt <owncloud instance>/index.php/s/XXXX
/a/owncloud/folder/file2.txt <owncloud instance>/index.php/s/XXXX
```
