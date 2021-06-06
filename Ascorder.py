def asc(i,b):
    
    m=b.copy()
    c=0
    for k in range(1, i):
        if b==m.sort:
            break
        elif b[0]>b[1]:
            b.remove(b[k-1])
        elif b[-1]<b[-2]:
            b.remove(b[-1])
            c+=1
    print(c)
    return c
    
    
    
i=int(input())
b=list(map(int, input().split() ))
print(asc(i,b))