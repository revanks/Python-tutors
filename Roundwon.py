def roundswon(N,S):
    
    a=0
    b=0
    for i in range(N):
        if ( ((a>=b and (S[i]=='W')))or((a<b)and (S[i]=='L'))):
            a+=1
        else:
            b+=1
    print(a, b)
    return a, b
    
N=int(input())
S=str(input())

print(roundswon(N,S))