import re


def read__goto(line):
    if 'goto' in line:
        return True
    else:
        print(line)
        return False
