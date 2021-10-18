num=int(input("Please input number "))
i=num
while i>0:
 if i%2==0:
   if i//2==1:
     print("Yes")
     break 
   i=i//2
 else:
  print("No")
  break