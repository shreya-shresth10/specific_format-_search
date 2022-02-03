from pathlib import Path
import os
from os import listdir
import sys
import fnmatch

path= ""
pattern= "*.*"

files = fnmatch.filter(os.listdir(path), pattern)
print(files)
