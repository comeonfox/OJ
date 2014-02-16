#!/usr/bin/env python
import cmexpr as cm
import sys
from random import choice
import string


def build(root, level):
    alphabet = string.lowercase
    ops = ('+', '-', '*', '/')

    if level == 1:
        root.fill(choice(alphabet))
        root.fill(choice(ops))
        root.fill(choice(alphabet))
        return

    l = cm.Tree()
    r = cm.Tree()
    root.fill(l)
    root.fill(choice(ops))
    root.fill(r)

    build(root.lc, level - 1)
    build(root.rc, level - 1)


def main(i, level):
    print i
    for t in xrange(i):
        root = cm.Tree()
        build(root, level)
        print root.flat()

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
