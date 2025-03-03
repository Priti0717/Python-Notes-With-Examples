#tuple:comma sep.value within ().
#It is ordered ,it is immutable,heterogeneous collection of elements,duplicates are allowed.

#how to access data from tuple:
#1)indexing 2)slicing

#1)indexing

t=(11,"raj","kunal",33)
print(t[2])#kunal
print(t[-3])#raj

#2)slicing:

t=(11,"raj","kunal",33)
print(t[1:3])#(raj ,kunal)

t=(11,22,33,44,[66,77,88])
print(t[-3::-1]) #(33,22,11)




