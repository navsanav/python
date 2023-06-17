import json
file=open("posts.json","r")
x=file.read()
filedata=json.loads(x)
print(filedata)
for a in filedata:
    print(a["name"])