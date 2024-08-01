cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities1.add("New York")
print(cities1)
#add() adds a single item in a set

cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities1.update(cities2)
print(cities1)
#update() addds more than one item


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities1.remove("Madrid")   
#remove() or discard() method removes items from list
#main difference between remove() and discard() is that if a certain element is not there remove gives error whereas discard does not give error
print(cities1)

cities1={"Tokyo","Madrid","Berlin","Delhi"}
item=cities1.pop()
#pop() removes the last item from the set and returns it
#if confused with the output remember sets are unordered
print(cities1)
print(item)

#del is not a method but a keyword whic deletes the set entirely
cities1={"Tokyo","Madrid","Berlin","Delhi"}
del cities1
#print(cities1) gives error as it has been deleted


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities1.clear()
#clear() removes all items from the set and returns empty set
print(cities1)



info={"Carla",19,False,5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")