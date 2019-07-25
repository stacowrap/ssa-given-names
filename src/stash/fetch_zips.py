#!/usr/bin/env python3
import requests
from mysettings import *

def fetch_zip(url):
    response = requests.get(url)
    if response.status_code != 200:
        msg = F"Status code {response.status_code} returned from {url}"
        Moggy.error(msg)
        raise RuntimeError(msg)
    else:
        Moggy.info(F"Downloaded {len(response.content)} bytes")
        return response.content


def main():
    for slug, url in SLUGS.items():
        Moggy.info(F"Downloading: {url}")
        zcontent = fetch_zip(url)

        zpath = ZIPS_DIR / F"{slug}.zip"
        Moggy.info(F"Stashing {zpath}")
        zpath.write_bytes(zcontent)


if __name__ == '__main__':
    Moggy.info("Fetching and saving files")
    initsettings()
    main()
