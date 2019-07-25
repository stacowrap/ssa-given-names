#!/usr/bin/env python3

"""
raw data:

PR,F,1998,Nicole,392
"""

import csv
import re
from mysettings import *


SRC_DIR = STASHED_DIR / 'territories'
DEST_PATH = COLLATED_DIR / 'territories.csv'


def main():
    srcfiles = sorted(SRC_DIR.glob('*.TXT'))
    Moggy.info(F"Found {len(srcfiles)} files in {SRC_DIR}")
    Moggy.info(F"From {min(srcfiles).stem} to {max(srcfiles).stem}")

    outf = DEST_PATH.open('w')
    outs = csv.DictWriter(outf, fieldnames=OUT_HEADERS)
    outs.writeheader()

    _tcount = 0
    for fn in srcfiles:
        for row in csv.reader(fn.open()):
            d = {}
            d['place'], d['gender'], d['year'], d['name'], d['count'] = row

            outs.writerow(d)
            _tcount += 1

            if _tcount > 0 and _tcount % 250000 == 0:
                Moggy.info(F"On file {fn.name}; collated {_tcount} rows")

    Moggy.info(F"Finished on file {fn.name}; collated a total of {_tcount} rows")
    outf.close()



if __name__ == '__main__':
    Moggy.info("Collating territory names")

    main()
