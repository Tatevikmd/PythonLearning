lis=list(input("Please input 10 numbers"))
l=list(input("Please input a search number"))
a=0
while a<len(lis):
  if lis[a]==l[0]:
    lis.remove (lis[a])
    print(lis)
  a=a+1
