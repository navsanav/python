d=[1,2,3,4,5,6,56,"ishu janeman"]
print(d[1:7])
print(d[-1])
print(d[0],d[2],d[3])
d.clear()
print(d)
d.append([1,2,3,4])
print(d)
print(d[0][3])
d.copy()
print(d)
d.append(10)
print(d,id(d))
b=d.pop(-1)
print(b)
print(d)