#how to add a data in set:
#1)add:Add an element to a set.This has no effect if the element is already present.
s={11,22,33,44}
s.add(55)
print(s)

#how to delete a data in set:
#1)remove():Remove an element from a set; it must be a member.If the element is not a member, raise a KeyError.

s={11,22,33,44}
s.remove(33)
print(s)

#s={11,22,33,44}
#s.remove(88)
#print(s)

#2)discard():Remove an element from a set if it is a member.
#Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.

s={11,22,33,44}
s.discard(33)
print(s)

s={11,22,33,44}
s.discard(77)
print(s)

#3)pop():it removes any random element from set and returns the removed element.

s={11,22,33,44}
s.pop()
print(s)

#4)clear():clear or delete all the data
s={11,22,33,44}
s.clear() #set()
print(s)

#intersection():Return the intersection of two sets as a new set.(i.e. all elements that are in both sets.)
s1={11,22,33,44}
s2={11,55,33,88}
s=s1.intersection(s2)
print(s)

#diffrence():Return the difference of two or more sets as a new set.(i.e. all elements that are in this set but not the others.)

s1={11,22,33,44}
s2={11,55,33,88}
s=s1.difference(s2)
print(s)

s1={11,22,33,44}
s2={11,55,33,88}
s=s2.difference(s1)
print(s)

#union():Return the union of sets as a new set.(i.e. all elements that are in either set.)
s1={11,22,33,44} 
s2={11,77,44,66}
s=s1.union(s2)
print(s)
# issubset():Report whether another set contains this set.
s1={11,22,33,44}
s2={11,22,33,44}
s=s1.issubset(s2)
print(s)

# issuperset():Report whether this set contains another set.
s1={11,22,33,44}
s2={11,22}
s=s1.issuperset(s2)
print(s)

#len(): function:Return the number of items in a container

s={11,22,33,44}
print(len(s))

#intersection_update():Update a set with the intersection of itself and another.
s1={11,22,33,44}
s2={11,77,44,66}
s1.intersection_update(s2)
print(s1)

#diffrence_update():Remove all elements of another set from this set.
s1={11,22,33,44}
s2={11,77,44,66}
s1.difference_update(s2)
print(s1)

#isdisjoint():have no elements in common
s1={11,22,33,44}
s2={121,228,334,43}
s=s1.isdisjoint(s2)
print(s)

#copy():Return a shallow copy of a set.
s={11,22,33,44}
s1=s.copy()
print(s1)

#update():Update a set with the union of itself and others.

s1={11,22,33,44}
s2={11,499,36,22}
s1.update(s2)
print(s1)