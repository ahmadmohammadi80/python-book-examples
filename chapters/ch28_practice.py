# Python book chapter 28, worked practice
import argparse
parser = argparse.ArgumentParser(prog="tasks")
parser.add_argument("action", choices=["add", "list", "done"])
parser.add_argument("--title", default="")
args = parser.parse_args(["add", "--title", "مطالعه"])
print(args.action, args.title)
