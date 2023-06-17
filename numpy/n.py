import numpy as np
n=np.array([1,2,3])
print(n)

n2=np.array([[1,2,3,4],[5,6,7,8]])
print(n2,type(n2))

n3=np.zeros((5,5))
print(n3)

n4=np.full((5,5),10)
print(n4)
n5=np.full((3,4),5)
print(n5)

s=np.arange(50,60)
print(s)
s1=np.arange(50,100,10)
print(s1)
s2=np.random.randint(100,200,10)
print(s2)