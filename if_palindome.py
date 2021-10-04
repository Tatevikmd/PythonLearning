n=1789871
i=n                                 
a=0
while n>0:
  b=n%10
  a=a*10+b
  n=n//10
if i==a:
    print("Yes")
else:
    print("No")
