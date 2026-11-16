"""Prints the 8.3 (short) spelling of the directory given as the argument.

Run: python -B .runs/author-fix-2/shorttmp.py <directory>   Exit code 0.
"""

import ctypes
import os
import sys

buffer = ctypes.create_unicode_buffer(500)
ctypes.windll.kernel32.GetShortPathNameW(os.path.abspath(sys.argv[1]), buffer, 500)
print(buffer.value)
sys.exit(0)
