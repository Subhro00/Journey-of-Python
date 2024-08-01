#dictionaries are ordered collection of data item,{} are used

dic={
    "Frank":"Human Being",
     "Spoon":"Object"
    }
print(dic)

d={
    280:"Frank",
    588:"Saggy",
    490:"Simpu",
    532:"Kirti"
}
#the dictionary consists of keys and value
#   Key:Value

print(d[532])


info={'name':"Frank",'age':19,'eligible':True}
print(info)
                                         #values in a dictionary can be accessed either by 
print(info["name"])                          #mentioning keys in square bracket
print(info.get('name'))                  #or using the get() method

#the only difference between [] and get() method is that if the value is not found it gives error in [] but return none in get()
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


print(info.items())

for key,value in info.items():
    print(f"The value correspondinf to the key {key} is {value}")



