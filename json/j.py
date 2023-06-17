import json
d={
    "name":"sandeep soni",
    "age":24                #dumps input json object lega or output string dega
                            #loads input string lega or output json object dega
}
f=json.dumps(d)
print(f,type(f))

z='[{"name":"sandeep","age":25}]'
x=json.loads(z)
print(x,type(x))

#for a in x:
    #print(a,x[a])

