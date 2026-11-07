# Python book chapter 28, example 1
import argparse

parser = argparse.ArgumentParser(description="فهرست کارها")
parser.add_argument("command", choices=["list", "add"])
parser.add_argument("title", nargs="?")
args = parser.parse_args(["add", "مطالعه پایتون"])
print(args.command, args.title)
