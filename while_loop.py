#syntax:
#i
#while condition:
#   body


#Wap to print sqr of numbers 1 to 10 by using while loop
# i=1
# while i<=10:
#     print(i**2)
#     i=(i)+1
    
#cube of number  in list 11 to 20
# i=11
# l=[]
# while i<=20:
#     cu=i**3
#     l.append(cu)
#     i=i+1
# print(l)

#squre of number  in dict 1 to 5
# i=1
# l={}
# while i<=5:
#     sq=i**2
#     l[i]=sq
#     i=i+1
# print(l)


#wap to print square of number by using while loop
# l=[1,2,3,4,5,6]
# i=0
# while i<len (l):
#     print(l[i]**2)
#     i=i+1

# l=["raj","pavan","vijay"]
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1

l=[1,2,3,4,5,6]
d={}
for i in l:
    sqr=i**2
    d[i]=sqr
print(d)
    
    