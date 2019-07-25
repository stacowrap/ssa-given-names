#!/usr/bin/env python3

import csv
from mysettings import *



DEST_PATH = WRANGLED_DIR / 'given-names.csv'



def main():
    outf = DEST_PATH.open('w')
    outs = csv.DictWriter(outf, fieldnames=OUT_HEADERS)
    outs.writeheader()

    for slug in SLUGS.keys():
        srcpath = COLLATED_DIR / F"{slug}.csv"
        with open(srcpath) as f:
            Moggy.info(F"Reading, sorting {srcpath}")
            data = sorted([row for row in csv.DictReader(f)],
                                key=lambda x: (x['place'], x['year'], x['gender'], -int(x['count']), x['name']))
            outs.writerows(data)

    outf.close()

if __name__ == '__main__':
    WRANGLED_DIR.mkdir(parents=True, exist_ok=True)
    main()
