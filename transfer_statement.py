#1)pass:

#WAP to check positive number

num=eval(input("enter the number :"))
if num >0:
    pass

#2)continue:current iteration skip
l=[11,22,33,44,55,66]
for i in l:
    if i%2==0:
        continue
    print(i)

#3)break:it break the loop, Terminate
l=[11,22,33,44]
for i in l:
    if num==22:
        break
    print(i)