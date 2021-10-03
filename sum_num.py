n=int(input())                          
sum=0                                    
i=n
while i>0:
  a=i%10
  sum=sum+a
  i=i//10
print(sum)