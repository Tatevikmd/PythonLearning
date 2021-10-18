l=[1,3,2,4,5]                             
i = 0
while(i< len(l)-1):
    j=i
    while (j<len(l)-1):
        if(l[i]>l[j+1]):
            a=l[j+1]
            l[j+1]=l[i]
            l[i]=a
        j=j+1
    i=i+1
print(l)