#if else statement:
#if condition:
#   body_if
#else:
#    body_else

# WAP to check number is positive or negative:

# num=eval(input("enter a number :"))
# if num > 0:
#     print("positive")
# else:
#     print("negative")

# WAP to check number is even or odd:

# num=eval(input("enter a num :"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

# WAP to print sqr of even numbers and cube of odd number from a given list :

# i=[1,2,3,4,5]
# for num in i:
#     if num %2==0:
#         print(num**2)
#     else:
#         print(num**3)

# WAP to print list of square of even numbers and list of cube of odd numbers from given list. 

# i=[1,2,3,4,5]
# even=[]
# odd=[]
# for num in i:
#     if num %2==0:
#         sq=num**2
#         even.append(sq)
#     else:
#         cube=num**3
#         odd.append(cube)
# print(even)
# print(odd)        

#WAP to print a dict of 

# student={"priti":40,"sid":99,"sonal":78,"yash":35}
# a=[]
# b=[]
# for name , per in student.items():
#     if per>40:
#         a.append(name)
#     else:
#         b.append(name)
# print(a)
# print(b)

#WAP to print dict of square of even and cube of odd numbers from 1 to 10

# a={}
# for num in range(1,11,1):
#     if num%2==0:
#         a[num]=num**2
#     else:
#         a[num]=num**3
# print(a)

# vivo={"v15":13000,"v16":25000,"v20":19000,"v24":27000}
# for model,price in vivo.items():
#     if price>20000:
#         vivo[model]=price-2000
#     else:
#         vivo[model]=price + 2000
# print(vivo)
        
# for name in vivo:
#     if vivo[name]>20000:
#         vivo[name]=vivo[name]-1000
#     else:
#         vivo[name]=vivo[name]+1000
# print(vivo)

# vivo={"v15":13000,"v16":25000,"v20":19000,"v24":27000}
# for i,j in vivo.items():
#     if j >20000 :
#         vivo[i]=vivo[i]-(j*(10/100))
#     else :
#          vivo[i]=vivo[i]-(j*(5/100))
# print(vivo)

