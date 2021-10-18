print("input 10 number")              
l=[]
for i in range(1,11,1):
  a=int(input())
  l.append(a)
print(l)
max=l[1]
for i in l:
  if i>max:
    max=i
print("Maximum number=",max)
min=l[1]
for i in l:
  if i<min:
    min=i
print("Minimum number=",min)
