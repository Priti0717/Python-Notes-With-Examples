#list is a comma sep. value within []
#It is ordered,mutable,hetrogeneous collection of element and duplictes are allowed.

# List
l=[12,14,13,16]
print(type(l))

#ordered:sequence is same as given.
l=[45,87,96]
print(l)

#hetrogeneous:we can store all fundamentaldata typrs and list,tuple,range,dict.
l=[12,'priti',[1,2,3,4],'12','[12,4,6]']
print(l)

#mutable:changeable
l=[25,45,65,34]
l.append(22)
print(l)

#immutable:not changeable
l="priti"
n=l.upper()
print(n)
#duplicates:double values are allow
l=[45,87,96,45,87]
print(l)

#indexing
l=[1,2,3,[11,22,33]]
print(l[-1][-3]) #11
print(l[3][2]) #33

l=[11,22,33,["raj","pavan"],66,[99,22]]
name=l[3][-1]
print(name.upper())  #PAVAN
 
#slicing
l=[11,22,33,["raj","pavan"],66,[99,22]]
n1=(l[3][0])
print(n1[::-1])#jar

l=[11,22,33,44,55,66]
print(l[1::2]) #22,44,66
print(l[-2::-2]) #55,33,11

l=[12,13,14,15,16]
print(l[-2:-5:-1]) #15,14,13

l=[11,22,33,[44,55,66],77,88,99]
print(l[1]+l[3][1]+l[5])#165

l2=[12,13,14,[78,79,80,81,[4,6,7,8]]]
print(l2[1])
print(l2[3][2])
print(l2[3][4][2])
print(l2[::2])
print(l2[3][1::2])
print(l2[3][4][::3])






