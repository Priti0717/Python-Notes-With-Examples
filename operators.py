#arthematic operator:

#pluse(+):it supports to string,
a=13
b=16
print(a+b)#29

a=23.98
b=34.98
print(a+b)#58.959999999999994

a="hello"
b="priti"
print(a+b)#hellopriti

a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)#[1, 2, 3, 4, 5, 6, 7, 8]

a=(1,2,3,4)
b=(5,6,7,8)
print(a+b)#(1, 2, 3, 4, 5, 6, 7, 8)

a=18+56j
b=14+54j
print(a+b)#(32+110j)

# a={1:"priti",2:"sid",3:"sonal",4:"radhika"}
# b={11:"priti",22:"sid",33:"sonal",44:"radhika"}
# print(a+b) #unsupported operand type(s) for +: 'dict' and 'dict'

# a={1,2,3,4}
# b={5,6,7,8}
# print(a+b) # unsupported operand type(s) for +: 'set' and 'set'


# minus(-):it only support numbers
a=13
b=16
print(a-b)

a=23.98
b=34.98
print(a-b)
#multiplication(*):

#division(/):it always give float number as output.

#floor division(//):it always return integer value as output .always take small value

print(-10//3)#-4

#module(%):
print(10 % 2)

#relational operator:>,<,<=,>=,==,!=:it gives output in bool

#logical operators:
#and:to connect two or more conditions. all true than true otherwise false.

print(True and True)

print(True and False)

print(False and True)

print(False and False)
#or:false false then false otherwise true.
print(True or True)

print(True or False)

print(False or True)

print(False or False)

#not:
print(not True)

print(not False)

#in operator:checks membership
i=[11,22,33,44]
print(33 in i)

#is operator:checks memory location is equal or not
s1=[11,22,33]
s2=[11,22,33]
print(s1 == s2)

s1=[11,22,33]
s2=[11,22,33]
print(s1 is s2)

s1=(11,22,33)
s2=(11,22,33)
print(s1 is s2)



