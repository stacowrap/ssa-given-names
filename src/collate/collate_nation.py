#!/usr/bin/env python3

"""
raw data:

    Emily,F,26539
    Hannah,F,21673
    Alexis,F,19234

Output:

    Text data, e.g.

    year,sex,name,count
    US,F,1999,Emily,26539
"""

import csv
import re
from mysettings import *


SRC_DIR = STASHED_DIR / 'nationwide'
DEST_PATH = COLLATED_DIR / 'nationwide.csv'


def main():
    srcfiles = sorted(SRC_DIR.glob('*.txt'))
    Moggy.info(F"Found {len(srcfiles)} files in {SRC_DIR}")
    Moggy.info(F"From {min(srcfiles).stem} to {max(srcfiles).stem}")

    outf = DEST_PATH.open('w')
    outs = csv.DictWriter(outf, fieldnames=OUT_HEADERS)
    outs.writeheader()

    _tcount = 0
    for fn in srcfiles:
        # fn.stem is `yob1999`
        year = re.search(r'\d{4}$', fn.stem)[0]
        for row in csv.reader(fn.open()):
            d = {'place': 'USA', 'year': year}
            d['name'], d['gender'], d['count'] = row

            outs.writerow(d)
            _tcount += 1

            if _tcount > 0 and _tcount % 250000 == 0:
                Moggy.info(F"On year {year}; collated {_tcount} rows")

    Moggy.info(F"Finished on year {year}; collated a total of {_tcount} rows")
    outf.close()



if __name__ == '__main__':
    Moggy.info("Collating nationwide names")

    main()
