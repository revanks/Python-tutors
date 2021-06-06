def Sumsmallergreaternumber(n, arr):
    dup=arr[:]
    dup.sort()
    dup.append(0)
    dup.insert(0,0)
    ans=[0]*n
    for i in range(1,n+1):
        s=dup[i+1]+dup[i-1]
        for j in range(n):
            if(arr[j]==dup[i]):
                ans[j]=s 
                break 
    print(*ans,end=" ")

n=int(input())
arr=list(map(int,input().split()))
print(Sumsmallergreaternumber(n, arr))