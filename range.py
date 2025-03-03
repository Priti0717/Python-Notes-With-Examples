# r=range(1,6,1)
# print(r)
# print(type(r))

# r=range(1,6,1)
# for num in r:
#     print(num)

# #write a program to print numbers from 11 to 20

# r=range(11,21,1)
# for num in r:
#     print(num)
    
# #write a program to print even numbers from 21 to 31

# r=range(22,31,2)
# for num in r:
#     print(num)
    
# #write a program to print odd numbers from 21 to 31

# r=range(21,32,2)
# for num in r:
#     print(num)
    
# #write a program to print a numbers from 31 to 21
# r=range(31,20,-1)
# for num in r:
#     print(num)
    
# #write a program to print a odd numbers from 50 to 30
# for num in range(49,30,-2):
#     print(num)
    
# #write a program to print a even numbers from 101 to 81
# for num in range(100,81,-2):
#     print(num)
    
# #write a program to print squere of a number 1 to 10
# for num in range(1,11,1):
#     print(num**2)
    
# #write a program to print list of a number 1 to 50
# l=[]
# for num in range(1,51,1):
#    l.append(num)
# print(l)

# #write a program to print list of odd a number 48 to 38
 
# l=[]
# for num in range(47,38,-2):
#    l.append(num)
# print(l)   

# #write a program to print set of square a number 10 to 20

# l=set()
# for num in range(10,21,1):
#     l.add(num**2)
# print(l)


# #write a program to print set of cube of  a even number 3 to 9

# l=set()
# for num in range(4,9,2):
#     l.add(num**3)
# print(l)


# #write a program to print dict of square of  a number 1 to 5

# sq={}
# for num in range(1,6,1):
#     l[num]=num**2
# print(sq)

# #write a program to print dict of cube of even  numbers of 5 to 11


# cube={}
# for num in range(6,11,2):
#     l[num]=num**3
# print(cube)

# employee={"priti":35000,"sonal":70000,"sid":98000,"radhika":56000}
# for num in employee:
#     employee[num]=employee[num]+2000
# print(employee)


# employee={}
# for i in range(10):
#     name=input("enter name :")
#     salary=eval(input("enter salary :"))
#     employee[name]=salary
# print(employee)  


# d={}
# for i in range(2):
#     details={}
#     roll=eval(input("enter roll no :"))
#     name=(input("enter name :"))
#     city=(input("enter city :"))
#     details["name"]=name
#     details["city"]=city
#     d[roll]=details
# print(d)


# employee={}
# for i in range(2):
#     details={}
#     id=eval(input("enter id :"))
#     name=(input("enter name :"))
#     city=(input("enter city :"))
#     salary=eval(input("enter salary :"))
#     department=(input("enter department :"))
#     details["name"]=name
#     details["city"]=city
#     details["salary"]=salary
#     details["department"]=department
#     employee[id]=details
# print(employee)

#details={1{name,city,percent,marks{1,2}},2{}}
# students={}
# for i in range(2):
#     details={}
#     marks={}
#     id=eval(input("enter id :"))
#     name=(input("enter name :"))
#     city=(input("enter city :"))
#     per=(input("enter per :"))
#     python=eval(input("enter python :"))
#     science=eval(input("enter science :"))
#     java=eval(input("enter java :"))
#     marks["python"]=python
#     marks["science"]=science
#     marks["java"]=java
#     details["name"]=name
#     details["city"]=city
#     details["per"]=per
#     details["marks"]=marks
#     students[id]=details
    
# print(students)

# mobile={}
# for i in range(2):
#     d={}
#     brand=(input("enter the brand :"))
#     price=eval(input("enter the price :"))
#     model=(input ("enter the model :"))
#     d["price"]=price
#     d["model"]=model
#     mobile[brand]=d
# print(mobile)


mobile={"oppo":{"ce2":{"storage":"128gb","price":23000,"ram":"164gb"},"ce3":{"storage":"128gb","price":23000,"ram":"164gb"}}}
mobile={}
for i in range(1):
    b={}
    details={}
    brand=input("enter brsnd: ")
    for j in range(2):
        model=input("enter the model :")
        storage=input("enter a storage :")
        price=eval(input("enter a price :"))
        ram=(input("enter a ram :"))
        details["storage"]=storage
        details["price"]=price
        details["ram"]=ram
        b[model]=details
    mobile[brand]=b
print(mobile)
    


    
    



