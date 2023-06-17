# A set is a collection which is unordered and unindexed,that is iterable,mutable,and has no duplicate elements.
#In python sets are written with curly brackets

s={10,20,30,40}
for a in s:
    print(a)
    

d=[1,2,3,4,5,6]
b=set(d) #set function kisi bhi datatype ko set me convert kar deta hai
print(b)
s={1,2,3,4,6,7}
s.remove(4)
print(s)
s.discard(5)
print(s)
s.pop()
print(s)
s.clear()
print(s)
s.add(70)
print(s)
p={10,20,60,70}
q={10,20,30}
p.update(q)
print(p)