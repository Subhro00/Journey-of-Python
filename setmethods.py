s1={1,2,5,6}
s2={4,3,6,7}
print(s1.union(s2))
#union()method prints all the items that are present in two sets,it returns a new set


s1.update(s2)
#update()method updates the original set with the items from another set
print(s1,s2)



cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.intersection(cities2)
#intersection prints only items that are similar to both the sets,it returns a new set
print(cities3)
cities1.intersection_update(cities2)
#intersection_update()method updates the original set with the items from another set
print(cities1,cities2)



cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.symmetric_difference(cities2)
#symmetric_difference() prints only the items that are not similar to both the sets,it returns a new set
print(cities3)
cities1.symmetric_difference_update(cities2)
#symmetric_difference_update()method updates the original set with the items from another set
print(cities1,cities2)



cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.difference(cities2)
#difference() prints only the items that are present in the first set but not in the second set,it returns a new set
print(cities3)
cities1.difference_update(cities2)
#difference_update()method updates the original set with the items from another set
print(cities1,cities2)