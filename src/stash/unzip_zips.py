#!/usr/bin/env python3

from shutil import unpack_archive
from mysettings import *


def main():
    for slug in SLUGS.keys():
        srcpath = ZIPS_DIR / F"{slug}.zip"

        destdir = STASHED_DIR / slug
        destdir.mkdir(parents=True, exist_ok=True)
        Moggy.info(F"Unpacking {srcpath} to {destdir}")

        unpack_archive(srcpath, extract_dir=destdir)


if __name__ == '__main__':
    Moggy.info("Unzipping zips")
    main()
