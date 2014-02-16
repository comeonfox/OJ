#coding: utf-8


ops = dict(zip(['#', '(', '+', '-', '*', '/'], [-2, -1, 0, 0, 1, 1]))


class exprTree(object):
    def __init__(self, lc, op, rc):
        self.backbone = [lc, op, rc]

    def str_recursive(self):
        oprank = dict(zip([None, '+', '-', '*', '/'], [2, 0, 0, 1, 1]))
        getop = lambda node: node.op if isinstance(node, exprTree) else None
        enclose = lambda node: '(' + str(node) + ')'
        left = enclose(self.lc) if oprank[getop(self.lc)] <  \
            oprank[self.op] else str(self.lc)
        if self.op in ('/', '-') and oprank[getop(self.rc)] == oprank[self.op]:
            right = enclose(self.rc)
        else:
            right = enclose(self.rc) if oprank[getop(self.rc)] <  \
                oprank[self.op] else str(self.rc)
        return left + str(self.op) + right

    def __str__(self):
        # non-recursive version
        oprank = dict(zip([None, '+', '-', '*', '/'], [2, 0, 0, 1, 1]))
        getop = lambda node: node.op if isinstance(node, exprTree) else None
        ret = ''
        nodes = [[self, 0]]
        while nodes:
            cur = nodes[-1]
            while cur[0] == ')':
                ret += cur
                nodes.pop()
                if nodes:
                    cur = nodes[-1]
                else:
                    cur = None
                    break

            if cur is None:
                continue
            if cur[1] == 0:
                while isinstance(cur[0].lc, exprTree):
                    nodes[-1][1] = 1
                    if oprank[cur[0].op] > oprank[cur[0].lc.op]:
                        ret += '('
                        nodes.append(')')
                    nodes.append([cur[0].lc, 0])
                    cur = nodes[-1]
                nodes[-1][1] = 1
                ret += str(cur[0].lc)
            else:
                cur = nodes.pop()[0]
                ret += str(cur.op)
                if cur.op in ('/', '-') and oprank[cur.op] == oprank[getop(cur.rc)]:
                    ret += '('
                    nodes.append(')')
                elif oprank[cur.op] > oprank[getop(cur.rc)]:
                    ret += '('
                    nodes.append(')')
                else:
                    pass
                if not isinstance(cur.rc, exprTree):
                    ret += str(cur.rc)
                else:
                    nodes.append([cur.rc, 0])
        return ret

    @property
    def op(self):
        return self.backbone[1]

    @property
    def lc(self):
        return self.backbone[0]

    @property
    def rc(self):
        return self.backbone[2]


def buildTree(expr):
    expr = expr.strip()
    operatorStack = ['#']
    oprandStack = []
    top = lambda stack: stack[-1]

    def _pop():
        op = operatorStack.pop()
        right = oprandStack.pop()
        left = oprandStack.pop()
        node = exprTree(left, op, right)
        oprandStack.append(node)

    for token in expr:
        if token in ops and token != '(':
            while ops[top(operatorStack)] >= ops[token]:
                _pop()
            operatorStack.append(token)
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            while top(operatorStack) != '(':
                _pop()
            operatorStack.pop()
        else:   # oprands
            oprandStack.append(token)
    operatorStack.pop(0)
    while operatorStack:
        _pop()
    return oprandStack[0]


def run(expr):
    t = buildTree(expr)
    print str(t)


if __name__ == '__main__':
    import sys
    t = int(sys.stdin.readline().strip())
    for i in xrange(t):
        expr = sys.stdin.readline().strip()
        run(expr)
