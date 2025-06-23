# # tuple = not modifiable
# mytup = (2,1,3.3)
# print(mytup)

# note: list ko tinaru methods haru matra tuple le suport garxa jasle tuple lai modify gardaina

# mytup.append(5) # not allowed
# print(mytup)

# # sorting
# # mytup.sort() #not allowed
# mytup = sorted(mytup) # allowed
# print(mytup)


# # set = unordered , mutable but contains immutable values which are unique , supports set operations
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)} # mutable data types set vitra huna paudaina

# # indexed based operation not supported
# print(myset[0])

# operations
# # add
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)}
# myset.add(5)
# print(myset)

# # remove
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)}
# myset.remove(1) # throws error if not found
# print(myset)

# # discard
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)}
# print(myset.discard(15)) # doesnot throw error if not found

# # finding
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)}
# print(2 in myset) 

# # copying
# myset = {1,2,1,"bigyan","bigyan",3.3,(1,2)}
# myset2 = myset.copy()
# myset.add(100)
# print(myset)
# print(myset2)

# # update
# myset = {1,2,1}
# myset.add((1,2,3,4))
# print(myset)
# # myset.update((3,4))
# # print(myset)

# # clear
# myset = {1,2,1}
# myset.clear()
# print(myset)


# # set operations
# set1 = {1,2,3,4}
# set2 = {3,4,5}
# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set2.isdisjoint(set1))
# print(set2.issubset(set1))
# print(set2.issuperset(set1))


# frozenset = immutable
set1 = {1,2,3,4}
fset1 = frozenset(set1)
set2 = {4,5,6,7}
fset2 = frozenset(set2)
print(fset1.union(fset2))