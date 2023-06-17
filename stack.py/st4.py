d=[]
while True:
    c=int(input('''
    1 push elements
    2 pop elements
    3 peek elements
    4 display stack
    5 exit
 '''))
    if c==1:
     n=input("enter the value")
     d.append(n)
     print(d)
    if c==2:
     p=d.pop()
     print(p)
     print(d)
    if c==3:
     print("peek elments",d[-1])
    if c==4:
     print("display stack",d)
    if c==5:
      break;

      
