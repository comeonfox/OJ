#!/usr/bin/env python
import sys
import copy


def rank(op1, op2, flag=False):
    if op1 is None or op2 is None:
        return 0
    op = dict(zip(['+', '-', '*', '/'], [0, 1, 2, 3]))
    ret = op[op1] / 2 - op[op2] / 2
    if flag:  # right oprand
        if op1 == '-' or op1 == '/':
            ret = op[op1] - op[op2] + 1
    return ret


class Tree(object):
    def __init__(self):
        self.backbone = [None] * 3  # left child, op, right child
        self.pointer = 0
        self.full = False
        self.ops = ('+', '-', '*', '/')

    def fill(self, tok):
        if tok == ')':
            self.full = True
        if self.full:
            return copy.deepcopy(self)
        if tok is None:
            raise TypeError
        if self.pointer < 3:
            if tok == '(':
                if self.pointer == 2:
                    self.fill(Tree())
                return
            if self.pointer < 1 and tok in self.ops:
                self.pointer = 1
            self.backbone[self.pointer] = tok
            self.pointer += 1
            return
        # pointer == 3
        if isinstance(self.rc, Tree):
            if self.rc.isfull:
                self.full = True
            else:
                self.rc.fill(tok)
        elif rank(self.op, tok) < 0:
            _tn = Tree()
            _tn.fill(self.rc)
            _tn.fill(tok)
            self.backbone[-1] = _tn
        else:
            self.full = True
            return copy.deepcopy(self)

    def clear(self):
        self.__init__()

    def flat(self, flag=0):
        l, o, r = ['', '', '']
        if isinstance(self.lc, Tree):
            l = self.lc.flat(rank(self.op, self.lc.op))
        if isinstance(self.lc, str):
            l = str(self.lc)
        if isinstance(self.op, str):
            o = str(self.op)
        if isinstance(self.rc, Tree):
            r = self.rc.flat(rank(self.op, self.rc.op, True))
        if isinstance(self.rc, str):
            r = str(self.rc)
        out = '(' + l + o + r + ')' if flag > 0 else l + o + r
        return out

    @property
    def isfull(self):
        return self.full

    @property
    def op(self):
        return self.backbone[1]

    @property
    def lc(self):
        return self.backbone[0]

    @property
    def rc(self):
        return self.backbone[2]


def getToken(expr):
    for t in expr.strip():
        yield t


def build(expr):
    tmpNode = Tree()
    for last in getToken(expr):
        ret = tmpNode.fill(last)
        if ret:   # means tmpNode is full
            tmpNode.clear()
            tmpNode.fill(ret)
            if last != ')':
                tmpNode.fill(last)
    return tmpNode


def main():
    t = int(sys.stdin.readline().strip())
    for i in xrange(t):
        expr = sys.stdin.readline().strip()
        t = build(expr)
        print t.flat()


if __name__ == '__main__':
    main()
