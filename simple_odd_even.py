n=int(input("Please, input number"))
i=2
while i<=n:
   #print(i)
  
   if n%i !=0:
     i=i+1
   else:
     if n // i ==1:
      print("Yes, the number is a simple")
      break
     else:
         print("No,the number isn't a simple")
         break


sum=0
for i in range(1,8):
  if i%2==0:
      print("even num =", i)
  else:
      print("odd num==",i)
for i in range(1,10):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print("simple num=",i)
    else:
        print("simple num=", i)
for i in range(1,10):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print("kataryal num=",i)


n=8
l=[]
simple_numbers=[]
even_numbers=[]
odd_numbers=[]
i=1
k=1
while i<=n:
    if i%2!=0:
      if i==1 or i==2:
        simple_numbers.append(i)
        i+=1
      while k<=i:
          if i//k==1:
              simple_numbers.append(i)
              break
          k+=1
      i+=1
    #elif

    if i%2==0:
        even_numbers.append(i)
        i+=1
    else:
        odd_numbers.append(i)
        i+=1

print("\n","simple_numbers=",simple_numbers,"\n","even_numbers=",even_numbers,"\n","odd_numbers=",odd_numbers)

print("\n","????_????=",????_????,"\n","?????_????=",?????_????,"\n","????_????=",????_????)