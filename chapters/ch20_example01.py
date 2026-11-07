# Python book chapter 20, example 1
import sys
from pathlib import Path

print("Python:", sys.version.split()[0])
print("Executable:", Path(sys.executable).name)
