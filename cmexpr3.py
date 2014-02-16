#!/usr/bin/env python


rank = dict(zip(['#', '(', '+', '-', '*', '/', None], [-2, -1, 0, 0, 1, 1, 2]))


def in2post(expr):
    ret = ''
    stack = ['#']
    for token in expr:
        if token == '(':
            stack.append(token)
        elif token in rank:
            while rank[stack[-1]] >= rank[token]:
                ret += stack.pop()
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                ret += stack.pop()
            stack.pop()
        else:
            ret += token
    while stack[-1] != '#':
        ret += stack.pop()
    return ret

enclose = lambda expr: '(' + expr + ')'
isexpr = lambda s: len(s) > 1


def post2in(expr):
    oprand = []
    operator = []
    for token in expr:
        if token in rank:
            r = oprand.pop()
            l = oprand.pop()
            if isexpr(r) and isexpr(l):
                opr = operator.pop()
                opl = operator.pop()
            elif isexpr(r):
                opr = operator.pop()
                opl = None
            elif isexpr(l):
                opl = operator.pop()
                opr = None
            else:
                opl, opr = [None, None]
            if rank[token] > rank[opl]:
                l = enclose(l)
            if rank[token] > rank[opr]:
                r = enclose(r)
            if rank[token] == rank[opr] and token in ['/', '-']:
                r = enclose(r)
            oprand.append(l + token + r)
            operator.append(token)
        else:
            oprand.append(token)
    return oprand[0]


def trans(expr):
    return post2in(in2post(expr.strip()))


if __name__ == '__main__':
    import sys
    t = int(sys.stdin.readline())
    for i in xrange(t):
        expr = sys.stdin.readline().strip()
        print trans(expr)
