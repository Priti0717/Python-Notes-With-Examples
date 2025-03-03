#billing system :

db={1:"poha",2:"upma",3:"dosa",4:"kachori",5:"vadapav",6:"tea",7:"misalpav",8:"coffee",9:"idli",10:"samosa"}
price={1:20,2:20,3:50,4:25,5:15,6:12,7:60,8:25,9:20,10:15}
items=[]
qu=[]
print("-"*95)
print(f" {" "*30} AMIROWALA HOTEL" )
print("-"*95)
while True:
    print(f" {" "*30} MENU")
    print("""
          1.poha       4.kachori      7.misalpav        10.samosa
          2.upma       5.vadapav      8.coffee
          3.dosa       6.tea          9.idli
          
          """)
    i=eval(input("enter your option :"))
    q=eval(input("enter quantity :"))
    items.append(i)
    qu.append(q)
    c=input("do you want to continue (y/n) :")
    if c=="n":
        print(f"-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Sr.no","Items","quantity","price","Total_amount"))
        print(f"-"*105)
        sum=0
        for i in range (len(items)):
             print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i+1,db[items[i]],qu[i],price[items[i]],price[items[i]]*qu[i]))
             print("-"*105)
             sum=sum+price[items[i]]*qu[i]
        print(f"your total amount is  {sum}")
        break
    

# db={1:"maggi",2:"nirma",3:"oil",4:"cadbury",5:"notebook",6:"salt"}
# price={1:25,2:90,3:2110,4:40,5:60}
# items=[]
# quantity=[]
# print("-"*100)
# print(f" {" "*40} DMART")
# print("-"*100)
# while True:
#     print(f"{" "*45} MENU")
#     print("""
#           1.maggi
#           2.nirma
#           3.oil
#           4.cadbury
#           5.notebook
#           """)
#     a=eval(input("enter the option :"))
#     q=eval(input("enter the quantity :"))
#     items.append(a)
#     quantity.append(q)
#     c=input("Do you want to continue (y/n) :")
#     if c=="n":
#         print("-"*100)
#         print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("Sr.no","items","quantity","price","total_amount"))
#         print("-"*100)
#         sum=0
#         for i in range (len(items)):
#             print("-"*100)
#             print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(i+1,db[items[i]],quantity[i],price[items[i]],price[items[i]]*quantity[i]))
#             print("-"*100)
#             sum=sum+price[items[i]]*quantity[i]
#         print(sum)
#         break
    
    
    
