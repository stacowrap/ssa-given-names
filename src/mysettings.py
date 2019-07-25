from pathlib import Path
import logging
from sys import stderr

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)

Moggy = logging.getLogger()
# Moggy.addHandler(logging.StreamHandler())


DATA_DIR = Path('data')
STASHED_DIR = DATA_DIR / 'stashed'
ZIPS_DIR = STASHED_DIR / 'zips'
COLLATED_DIR = DATA_DIR / 'collated'
WRANGLED_DIR = DATA_DIR / 'wrangled'

OUT_HEADERS = ['place', 'year', 'name', 'gender', 'count']



SLUGS = {
    'nationwide': 'https://www.ssa.gov/oact/babynames/names.zip',
    'states': 'https://www.ssa.gov/oact/babynames/state/namesbystate.zip',
    'territories': 'https://www.ssa.gov/oact/babynames/territory/namesbyterritory.zip',

}


def initsettings():
    for p in [STASHED_DIR, COLLATED_DIR, WRANGLED_DIR, ZIPS_DIR]:
        p.mkdir(exist_ok=True, parents=True)
