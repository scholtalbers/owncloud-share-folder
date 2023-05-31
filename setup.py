from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="owncloud-share",
    version="1.0.0",
    author="Jelle Scholtalbers",
    author_email="j.scholtalbers@gmail.com",
    install_requires=requirements,
    extras_require={
        "dev": ["setuptools"]
    },
    entry_points={
        "console_scripts": [
            "oc-share = oc_share:main",
        ],
    },
    url="https://github.com/scholtalbers/owncloud-share-folder/",
    description="Quick public sharing of OwnCloud files."
)
