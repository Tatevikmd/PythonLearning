x=int(input("Please input number"))
i=x
num_bin=""
while i>0:
  a=i%2
  num_bin+=str(a)
  i=i//2
print(num_bin)
