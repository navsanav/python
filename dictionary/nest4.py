d={
'a':{"name":"bhanwari devi soni","age":"70","role":"dadi"},
'b':{"name":"ashok kumar soni","age":"53","role":"father"},
'c':{"name":"ratni devi soni","age":"45","role":"mother"},
'd':{"name":"sandeep soni","age":"25","role":"me"},
'e':{"name":"pooja soni","age":"25","role":"badi behan"},
'f':{"name":"minku soni","age":"18","role":"choti behan"}
}

print(d['a']["role"])
for k,l in d.items():
    print(k,l["name"],l["role"])
    d["d"]["age"]="30"
    print(d["d"])
    del([ d["d"]["age"]])
    print(d)