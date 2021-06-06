def sumof(lst, leng):
    new_lst=[]
    leng=len(lst)
    lst.sort()
    for i in range(0, leng):
        sum=0
        if i==0:
            sum=0+lst[i+1]
        elif i==leng-1:
            sum=0+lst[i-1]
        else:
            sum=lst[i+1]+lst[i+1]
        print(lst[i])
        new_lst.append(sum)
    print(new_lst)

lst=[1,5,2,3,8]
leng=len(lst)
print(sumof(lst, leng))