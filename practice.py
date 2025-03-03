# #area of rectangle:

# l=eval(input("enter length :"))
# w=eval(input("enter width :"))
# area=l*w
# print(area)

# #simple intrest calculation:

# p=eval(input("enter principle amount :"))
# r=eval(input("enter rate of intrest :"))
# t=eval(input("enter time period :"))
# simpleintrest=p*(r/100)*t
# print(simpleintrest)

# #perimeter of a square:
# side=eval(input("enter the length of side :"))
# perimeter= (4*side)
# print(perimeter)

# #calculate body mass index

# w=eval(input("enter the weight (kg) :"))
# h=eval(input("enter the height(m) :"))
# BMI=w/(h**2)
# print(BMI)

# #area of circle
# r=eval(input("enter the are of circle :"))
# area=3.14*r**2
# print(area)

# #convert minute to seconds
# m=eval(input("enter the number of min:"))
# seconds=m*60
# print(seconds)

# #speed calculation
# d=eval(input("enter the distance traveled :"))
# t=eval(input("enter the time taken :"))
# speed=d/t
# print(speed)

# #calculation average of three numbers
# m=eval(input("enter the number :"))
# m1=eval(input("enter the number :"))
# m2=eval(input("enter the number :"))
# average=(m+m1+m2)/3
# print(average)

# #calculate compound intrest
# #p=eval(input("enter the princpal :"))


# name="priti"
# s=set(name)
# print(s)

# s1={11,22,33,44}
# s2={11,77,44,66}
# s=s1.intersection(s2)
# print(s)

# s1={11,22,33,44}
# s2={11,77,44,66}
# s=s1.difference(s2)
# print(s)

# s1={11,22,33,44} #Return the union of sets as a new set.(i.e. all elements that are in either set.)
# s2={11,77,44,66}
# s=s1.union(s2)
# print(s)

# s1={11,22,33,44} #Report whether another set contains this set.
# s2={11,22,33,44}
# s=s1.issubset(s2)
# print(s)

# s=[11,22,33,22,44,11]
# p=set(s)
# print(p)

# s={11,22,33,44}
# print(len(s))

# s={11,22,33,44}
# s.add(55)
# print(s)

# s1={11,22,33,44}
# s2={11,77,44,66}
# s1.intersection_update(s2)
# print(s1)

# s1={11,22,33,44}
# s2={11,77,44,66}
# s1.difference_update(s2)
# print(s1)

# s={11,22,33,44}
# s.remove(44)
# print(s)

# s1={11,22,33,44}
# s2={121,228,334,43}
# s=s1.isdisjoint(s2)
# print(s)

# s={11,22,33,44}
# s.clear()
# print(s)

# s={11,22,33,44}
# s1=s.copy()
# print(s1)

# s={11,22,33,44}
# s.pop()
# print(s)

# s1={11,22,33,44}
# s2={11,499,36,22}
# s1.update(s2)
# print(s1)

# s=(11,22,33)
# from sys import getsizeof
# print(getsizeof(s))

# s=[11,22,33]
# from sys import getsizeof
# print(getsizeof(s))

# a = 5
# b = 10
# if a > b or a == 5:
#     print("X")
# else:
#     print("Y")

# print(0xA + 0xB + 0xC)


a=[ ]
for i in d:
      if d[i]>30000:
            a.append(i)
            print(a)
