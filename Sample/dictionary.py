d = {"Roll no": 52, "name": "samuel j", "grade": "A","age":21,"age":22}
print(d)
print(d["Roll no"])
print(len(d))

#get methode to access items
print(d.get("name"))

#access keys
print(d.keys())

#add new item
d["height"]=183
print(d)

#loop through dictionary keys and values
for i in d:
    print(i)
    print(d[i])

for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)


#copy dictionary
dict1=d.copy()
print(dict1)
dict2=dict(dict1)
print(dict2)

#nested dictionary
d2={1:{"Roll no": 52, "name": "samuel j", "grade": "A","age":21,"age":22},
    2:{"Roll no": 52, "name": "samuel j", "grade": "A","age":21}}
print(d2[1]["name"])
print(d2[2])
