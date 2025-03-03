#methods of list
#how to add data into list?
#1)append 2)insert
#1)append():Append object to the end of the list
name=["priti","jaysing","patil"]
name.append("jbk")
print(name)
name.append("kolhapur")
print(name)

numbers=[11,22,33,[44,55,66],77,88]
numbers.append(999)
print(numbers)
n1=numbers[3] #numbers[3].append(888)
n1.append(888)
print(n1)
print(numbers)

numbers=[11,22,33,[44,55,66,["raj","pavan"]],77,88]
numbers[3][3].append("priti")
print(numbers)

#insert():Insert object before index.
name=["priti","patil"]
name.insert(1,"jaysing")
print(name)

l=[11,22,33,[44,55,66],88,99]
n1=l[3] #l[3].insert(2,888)
n1.insert(2,888)
print(n1)
print(l)

#how to delete data from list
#1)remove():It takes value and it remove 1st value in case of duplicates.It dosent give return value.
#Remove first occurrence of value.Raises ValueError if the value is not present 
l=[11,22,33,44]
l.remove(22)
print(l)

l=[11,22,33,[44,55,66,[888,666,552]]]
l[3].remove(44)
print(l)
l[3][2].remove(666)
print(l)

l=["priti","sonal","priti"]
l.remove("priti")
print(l)
 
#2)pop():It takes index number.If we keep empty then it will delete last .default value(-1)
#It give delete value in return.Remove and return item at index (default last).
#Raises IndexError if list is empty or index is out of range.
l=[11,22,33,22,44]
l.pop(-2)
print(l)

l=[11,22,33]
l1=[]
l1.append(l.pop())
print(l)
print(l1)

#3)clear():clear or delete all the data
l=[111,222,333,444]
l.clear()
print(l)

#4)del:kryword to delete.
l=[111,222,333,444]
del l[1]
print(l)

#copy():Return a shallow copy of the list.
l1=[11,22,33,44]
l2=l1
print(l2)#[11, 22, 33, 44]
l2.append(55)
print(l2)#[11, 22, 33, 44, 55]
print(l1) #[11, 22, 33, 44, 55]


l1=[11,22,33,44]
l2=l1.copy()
l2.append(55)
print(l2) #[11, 22, 33, 44, 55]
print(l1) #[11, 22, 33, 44]
print(id(l1)) #2197611738432
print(id(l2)) #2197611687872

#extend():Extend list by appending elements from the iterable.
l1=[11,22,33]
l2=[44,55,66]
l1.extend(l2)
print(l1)

#count():Return number of occurrences of value.
l=[11,22,33,44,11,55,11]
print(l.count(11))

#index():Return first index of value.Raises ValueError if the value is not present.
l=[11,22,33,55]
print(l.index(55))

#reverse():
l=[11,22,33,44]
l.reverse()
print(l)

#sort():It is a method of a list .
l=[11,22,33,44]#it do changes in orignal object.
l.sort()#it does not give return.
print(l)

#sorted():it is function.
l=[44,55,33,11] #it do  not change in orignal object.
print(sorted(l))#it give return.
print(l)

#update():syntax:var[index]=update value.
l=[11,22,33,44]
l[2]=333
print(l)

l=[11,22,[33,44],55,66]
l[2][1]=444
print(l)

