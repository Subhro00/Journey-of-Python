set1={2,4,2,6}
#sets are unordered collection of data items it stored multiple items in a single variable .sets are kept inside {}
print(set)
#sets are unchangeable after creation
#lists - ()
#tuple - []
#sets  - {}
#dict - {}

info={"Frank",19,False,5.9,19}
print(info)     #the order is not maintained and gets printed randomly

s={}    #this is not a set it is a dict
print(s,type(s))
r=set()
print(r,type(r))  #this is a set or rather an empty set

for value in info:
    print(value)  #type of each value in the set is different