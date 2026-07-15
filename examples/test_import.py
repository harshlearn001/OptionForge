import os
import sys

print("cwd:", os.getcwd())
print("file:", __file__)
print("sys.path[0]:", sys.path[0])

import optionforge

print("SUCCESS:", optionforge.__file__)