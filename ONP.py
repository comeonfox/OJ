import sys
def onp(expr, stack = []):
    ''' the main logic of the onp problem.
        this logic doesn't check for syntax
        errors. '''
    que = list(expr)
    block = []                          # temporarily used
    for ch in que:
        if ch == ')':
            while stack[-1] != '(':
                block.append(stack.pop())
            stack.pop()
            block.reverse()
            stack.append(process(block)) # change the notation form
            del block[:]  # clean block
        else:
            stack.append(ch)
    return  stack.pop()

def process(block, operators='+,-,*,/,^'.split(',')):
    ''' change the notation form.
        process(list)-->str '''
    #if __name__ == '__main__':
    #    pdb.set_trace()
    if block[1] in operators:
        temp = block[1]
        del block[1]
        block.append(temp)
    else:
        sys.stderr.write("Err: element number of block is %d.\n" % len(block))
        print '|'.join(block)
    return ''.join(block)

def main():
    casen = int(sys.stdin.readline())
    while casen:
    expr = sys.stdin.readline().strip('\n')
        print onp(expr)
        casen -= 1
if __name__ == '__main__':
    main()
    li = list("abc")
