cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.isdisjoint(cities2))
#isdisjoint() checks if items of given set are present in another set,the method returns false if present else true



cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.issuperset(cities2))
#issuperset() checks if items of given set are present in another set,the method returns true



cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.issubset(cities2))
#issubset() checks if items of given set are present in another set,the method returns false


# Disjoint Sets:
# Two sets are said to be disjoint if they have no elements in common.
# In other words, the intersection of the two sets is empty.

# Subset:
# A set A is said to be a subset of a set B if every element of A is also an element of B.

# Superset:
# A set A is said to be a superset of a set B if every element of B is also an element of A.