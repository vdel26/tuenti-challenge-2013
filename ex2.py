#!/bin/env python

import fileinput


def seek(word, dictname):
    with open(dictname, 'r') as wordlist:
        sword = sorted(word)
        a = []
        for entry in wordlist:
            if word != entry.rstrip('\n'):
                if sword == sorted(entry.rstrip('\n')):
                    a.append(entry.rstrip('\n'))
    return a


def beautify(word, acronyms):
    s_acronyms = sorted(acronyms)
    print "%s -> %s" % (word, ' '.join(s_acronyms))


if __name__ == '__main__':
    for line in fileinput.input():
        linenum = int(fileinput.lineno())
        line_clean = line.rstrip('\n')
        if linenum == 2:
            dictname = str(line_clean)
        elif linenum == 4:
            numwords = int(line_clean)
        elif line_clean[0] is not '#':
            word = str(line_clean)
            acronyms = seek(word, dictname)
            beautify(word, acronyms)
