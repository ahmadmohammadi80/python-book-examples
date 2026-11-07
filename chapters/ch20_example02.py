# Python book chapter 20, example 2
from importlib import metadata

package_name = "pip"
try:
    print(package_name, metadata.version(package_name))
except metadata.PackageNotFoundError:
    print("بسته در این محیط نصب نیست")
