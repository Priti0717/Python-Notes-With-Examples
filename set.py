#set: It is a comma sep.value within {}.
#it is unordered,mutable,heterogeneous collection of immutable element,duplicates are not allowed.

s={11,11.3,3+5j,True,"priti"}
print(s)

#s={11,11.3,3+5j,True,"priti",[11,22,"priti"]}
#print(s) #unhashable type: 'list'

#s={11,11.3,3+5j,True,"priti",{11,22,"priti"}}
#print(s) #unhashable type: 'set'

s={11,11.3,3+5j,True,"priti"} #mutable
s.add("sonal")
print(s)
print(id(s))

#s="priti jaysing patil" #immutable 
#s.replace("r",i)
#print(s)

s="priti jaysing patil"
s1=s.replace("p","s")
print(s1)
print(s)
print(id(s))#2359898916464
print(id(s1))#2359898880624

s={11,11.3,3+5j,True,"priti",11}
print(s)

#empty set : s=set()
#s1=set([11,22,[1,2]])
#print(s1) #unhashable type: 'list'

s=set([11,22,33,44])
print(s) #{11,22,33,44}

s=set()
print(type(s)) #<class 'set'>

s={}
print(type(s)) #<class 'dict'>