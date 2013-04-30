#!/bin/env python

import fileinput


def find(word):
    pass


if __name__ == '__main__':
    for line in fileinput.input():
        linenum = int(fileinput.lineno())
        line_clean = line.rstrip('\n')
        if linenum == 2:
            dictname = str(line_clean)
            print dictname
        elif linenum == 4:
            numwords = int(line_clean)
            print numwords
        elif line_clean[0] is not '#':
            word = str(line_clean)
            print "word"
