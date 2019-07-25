# This boilerplate snippet puts the src/ directory
# into the system path so that the Python interpreter knows that:
#
#     import mysettings
#
# ...refers to:
#
#     import src.mysettings
import os
import sys
_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, _ROOT)


import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
