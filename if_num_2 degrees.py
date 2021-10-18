num=int(input("Please input number "))
i=num
while i>0:
 if i%2==0:
   if i//2==1:
     print("Yes, the number is 2 degrees.")
     break 
   i=i//2
 else:
  print("No, the number is not 2 degrees.")
  break