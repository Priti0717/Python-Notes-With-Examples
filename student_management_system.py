db={}
print("-"*106)
print(f"{" "*40}THE KIRAN ACADEMY")
print("-"*106)
while True:
    print(f""" 
        {" "*35} DASHBOARD
        {" "*15} 1.Add Student Details
        {" "*15} 2.Display Student Details
        {" "*15} 3.Update Student Details
        {" "*15} 4.Delete Student Details
        {" "*15} 5.Filter
        {" "*15} 6.Exit
        
        
        """)
    ch=eval(input("enter the choice :"))
    if ch==1:
        roll=eval(input ("enter your roll number : "))
        name=(input ("enter your name : "))
        city=(input ("enter your city : "))
        per=eval(input ("enter your percentage : "))
        db[roll]={"name":name,"city":city,"percentage":per}
        print(db)
    elif ch==2:
        print("_"*86)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("roll no","name","city","percentage"))
        print("_"*86)
        for roll in db:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll,db[roll]["name"],db[roll]["city"],db[roll]["percentage"]))
            print("-"*86)
            
    elif ch==3:
        roll=eval(input("enter roll number :"))
        print("""
              1.name
              2.city
              
              3.percentage
              """)
        u=eval(input("enter the choice :"))
        if u==1:
            name=input("enter the updated name :")
            db[roll]["name"]=name
            print(" Name Updated Successfully")
        elif u==2:
            city=input("enter the updated city :")
            db[roll]["city"]=city
            print("City Updated Successfully")
        elif u==3:
            per=input("enter the updated percentage :")
            db[roll]["percentage"]=per
            print("Percentage Updated Successfully")
        else:
            print("invalid")       
    elif ch==4:
        a=eval(input("enter roll number :"))
        db.pop(a)
        
    elif ch==5:
        
        
        city=input("enter the city :")
        per=eval(input("enter the percentage :"))
        filtered_students = {roll: details for roll, details in db.items() if details["city"] == city and details["percentage"] >= per}
        print("_"*86)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("roll no","name","city","percentage"))
        print("_"*86)
        for roll in filtered_students:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll,filtered_students[roll]["name"],filtered_students[roll]["city"],filtered_students[roll]["percentage"]))
            print("-"*86)

            break
    else:
        print("invalid")
        
        
    
# db={}
# print("-"*106)
# print(f"{" "*40}VIPRO")
# print("-"*106)
# while True:
#     print(f""" 
#         {" "*35} DASHBOARD
#         {" "*15} 1.Add Employee Details
#         {" "*15} 2.Display Employee Details
#         {" "*15} 3.Update Employee Details
#         {" "*15} 4.Delete Employee Details
#         {" "*15} 5.Filter
#         {" "*15} 6.exit
        
#         """)
#     ch=eval(input("enter the choice :"))
#     if ch==1:
#         id=eval(input ("enter your id : "))
#         name=(input ("enter your name : "))
#         city=(input ("enter your city : "))
#         department=input ("enter your department : ")
#         db[id]={"name":name,"city":city,"department":department}
#         print(db)
#     elif ch==2:
#         print("_"*86)
#         print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("id","name","city","department"))
#         print("_"*86)
#         for id in db:
#             print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(id,db[id]["name"],db[id]["city"],db[id]["department"]))
#             print("-"*86)
            
#     elif ch==3:
#         id=eval(input("enter id :"))
#         print("""
#               1.name
#               2.city
#               3.department
#               """)
#         u=eval(input("enter the choice :"))
#         if u==1:
#             name=input("enter the updated name :")
#             db[id]["name"]=name
#             print(" Name Updated Successfully")
#         elif u==2:
#             city=input("enter the updated city :")
#             db[id]["city"]=city
#             print("City Updated Successfully")
#         elif u==3:
#             per=input("enter the updated department :")
#             db[id]["percentage"]=per
#             print("department Updated Successfully")
#         else:
#             print("invalid")       
#     elif ch==4:
#         a=eval(input("enter id number :"))
#         db.pop(a)
        
#     elif ch==5:
#         city=input("enter the city")
#         per=eval(input("enter the "))
#         break
#     else:
#         print("invalid")

