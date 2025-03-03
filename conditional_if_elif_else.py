#for multiple condition.
#if cond1:
#   body_if
#elif cond2:
#   body_elif
#else:
#   body_else

# num=eval(input("enter the num :"))
# if num ==0:
#     print("zero")
# elif num > 0:
#     print("positive")
# else:
#     print("negative")


#grades
# marks=eval(input("enter the marks :"))
# if marks>90:
#     print("A+")
# elif marks > 80 :
#     print("A")
# elif marks > 70:
#     print("B+")
# elif marks > 60 :
#     print("B")
# else:
#     print("C")


#calculator:
# num1=eval(input("enter a number :"))
# num2=eval(input("enter a number :"))
# opr=(input("enter the operator :"))
# if opr == '+':
#     print(num1+num2)
# elif opr == '-':
#     print(num1-num2)
# elif opr == '*':
#     print(num1*num2)
# elif opr == '/':
#     print(num1/num2)
# elif opr == '%':
#     print(num1%num2)
# else:
#     print("invalid statement.")

#month:
# month=eval(input("enter the month : "))
# if month == 1:
#     print("jan")
# elif month == 2:
#     print("feb")
# elif month == 3:
#     print("march")
# elif month == 4:
#     print("april")
# elif month == 5:
#     print("may")
# elif month == 6:
#     print("june")
# elif month == 7:
#     print("july")
# elif month == 8:
#     print("aug")
# elif month == 9:
#     print("sep")
# elif month == 10:
#     print("oct")
# elif month == 11:
#     print("nov")
# elif month == 12:
#     print("dec")
# else:
#     print("invalid")    
    
#age:
# age=eval(input("enter the age :"))
# if age < 16:
#     print("Child")
# elif age < 50:
#     print("Adult")
# elif age >=50:
#     print("old")

#logical operator:
# p=eval(input("enter age of p :"))
# r=eval(input("enter age of s :"))
# s=eval(input("enter age of s :"))
# if p > s and p > r:
#     print("priti is bigger !")
# elif s > p and s > r:
#     print("sid is bigger !")
# else :
#       print("rohan is bigger !")


# w=eval(input("enter the weight :"))
# d=(input("enter the destination :"))
# if d == "domestic" :
#     if w <= 5:
#         print("cost : 10 rs")
#     elif w <=20:
#          print("cost : 20 rs")
#     else:
#         print("cost : 30 rs")
# elif d== "international":
#     if w<=5:
#          print("cost : 30 rs")
#     elif   w<=20:
#          print("cost : 50 rs")
#     else :
#          print("cost : 70 rs")
        
        
# salary=eval(input("enter the salary :"))
# if salary<10000:
#     print("no income tax :")
# elif salary<30000:
#     print("you income tax is :",(salary-10000)*(0.1))
# elif salary<70000:
#     print("you income tax is :",(salary-30000)*(0.2)+2000)
# else:
#     print("you income tax is :",(salary-70000)*(0.3)+10000)


# purchase_amount=eval(input("enter the purchase_amount :"))
# if purchase_amount>=500:
#     print((purchase_amount*20)/100)
# elif purchase_amount>=200:
#     print((purchase_amount*10)/100)
# elif purchase_amount<200:
#     print("no discount")

# num=eval(input("enter a number :"))
# if num==12 or num==1 or num==2:
#     print("spring")
# elif num==3 or num== 4 or num==5:
#     print("winter")
# elif num==6 or num==7 or num==8:
#     print ("summer")
# elif num==9 or num==10 or num==11:
#     print ("autum")

#electricity bill :


# unit=eval(input("enter the unit consumed :"))
# if unit >=100:
#     print(0.5*unit)
# elif unit>=200:
#     print(0.75*unit)
# elif unit >=300:
#     print(1.20*unit)
    
#movie ticket :

# age=eval(input("enter the age : "))
# time=eval(input("enter the time : "))
# if age<12:
#     print("rs 12 !")
# elif age>60:
#     print(" rs 6 !")
# elif age>12 :
#     if time ==10 or time ==11 or time==12 or time==1 or time ==2 or time==3 or time==4:
#         print("rs 7 !")
#     else:
#         print("rs 10")


# Problem Statement: Determine the type of triangle based on the lengths of its sides. The types are: Equilateral if all sides are equal, Isosceles if exactly two sides are equal, and Scalene if all sides are different.

# a=eval(input("enter a :"))
# b=eval(input("enter b :"))
# c=eval(input("enter c :"))
# if a==b and b==c:
#     print("equilateral ")
# elif a==b or b==c :
#     print("isosceles")
# else:
#     print("scalene")



#Problem Statement: Determine the day of the week based on a given number (1-7). The mapping is: 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, and 7 for Sunday.

# day=eval(input("enter a  day :"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#     print(" Wednesday")
# elif day==4:
#     print(" Thursday")
# elif day==5:
#     print(" Friday")
# elif day==6:
#     print("Saturday")
# elif day==7:
#     print(" Sunday")
# else:
#     print("invalid")


#Problem Statement: Calculate the fare for a taxi ride based on the distance traveled. The fare is $20 for the first 5 kilometers, $2 per kilometer for the next 10 kilometers, and $3 per kilometer for distances over 15 kilometers
 
# d=eval(input("enter the distance :"))
# if d==5:
#     print(" 20 rs ")
# elif d<15:
#     print(d*2)
# elif d>=15:
#     print(d*3)

#interest

# balance=eval(input("enter the balance :"))
# account=(input("enter the account :"))
# if account=="regular":
#     if balance<=10000:
#         print(balance*0.03)
#     elif balance>10000:
#         print(balance*0.04)
# elif account=="premium":
#     print(balance*0.05)

# color=input("enter the color :")
# size=input("enter the size :")
# if color=="red" and size=="medium_size":
#     print("apple")
# elif color=="yellow" and size=="long":
#     print("banana")
# elif color=="red" and size=="small":
#     print("cherry")
# else:
#     print("invalid")


