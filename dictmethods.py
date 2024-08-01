ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}

ep1.update(ep2)
#updates the ep1 dictionary with the keys and values of ep2
print(ep1,'\t\t',ep2)

ep2.clear()
#clears the ep2 dictionary
print(ep2)

empt={}
print(empt)

ep1.pop(122)
#pop() method removes the key-value pair whose key is used in as parameter
print(ep1)

ep1.popitem()
#popitem() method removes the last key-value pair from the dictionary
print(ep1)


#del ep1

#del deletes the dictionary entirely

del ep1[123]
print(ep1)

