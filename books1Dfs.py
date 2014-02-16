def evaluate(pages,border, avg):
    D =0
    for i in range(len(border)):
        d =  sum(pages[border[i-1][0]:border[i][0]]) - avg
        D += d**2
    return D

def DFS(k, m, pages,solutions, border,branch=-1,score = [float("inf"),0]):
    import pdb
    pdb.set_trace()
    if branch != 0:
        if branch == -1:
            branch = 0
        avg = sum(pages)/m
        total =0
        start =branch
        for i in range(branch,len(pages)):
            total += pages[i]
            if total < avg and i==len(pages)-2:
                border.append([start,'<'])
                total =0
                start=i+1
            if total > avg:
                border.append([start,'>'])
                total=0
                start = i+1
            if total == avg:
                border.append([start,'='])
                total=0
                start = i+1
        if len(border) == m-1:
            border.append([start,'<'])
        # evaluate the solution
        temp = evaluate(pages, border, avg)
        # save the solution
        solutions.append([])
        solutions[-1]=border[:]
        if temp == 0:
            return solutions[-1]
        else :
            if temp  < score[0] :
                score[0]=temp
            # search back
            nxt = border.pop()
            while len(border)>0 and border[-1][1]!='>':
                nxt = border.pop()
            if len(border)>0:
                if border[-1][0]>0:
                    border[-1][0] -= 1
                border[-1][1] = '<'
                # modify branch
                branch = nxt[0] - 1
                DFS(k, m, pages,solutions,border,branch, score)
            else:
                return solutions[score[1]]
s = []
b=[]
print DFS(5,3,[1,2,3,4,5],s,b)
