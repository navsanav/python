a=(1,2,3,4,5,6,78)
print(a[0],a[5])
l=len(a)
print(l)
for o in range(l):
    print(a[o])
    b=max(a)
    print(b)
    c=min(a)
    print(c)
    s=sum(a)
    print(s)
    m=a.count(2)
    print(m)
    f=a.index(3)
    print(f)

    print(a[-1::-2])

