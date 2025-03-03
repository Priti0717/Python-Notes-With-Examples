#complex
p=10+24j
print(type(p))
print(p.real)# real part of complex
print(p.imag)# imag part of complex


# binary= contain 0 and 1 value.(base2) 
num=0b101010 
print(num) #42

#num1=0b1200
#print(num1)


#bin()=Return the binary representation of an integer.covert decimal number in binary.
p=19
print(bin(p)) #0b10011

s=45
print(bin(s)) #0b101101

num=69
print(bin(num)) #0b1000101

k=7
print(bin(k)) #0b111

d=110
print(bin(d)) #0b1101110

#octal=value contains between 0 to 7. (base 8)

num=0o1754
print(num) #1004

#oct()=Return the octal representation of an integer. converts decimal number in octal.

n=14
print(oct(n)) #0o16

p=6
print(oct(p)) #0o6

h=76
print(oct(h)) #0o114

priti=30
print(oct(priti)) #0o36

s=15
print(oct(s)) #0o17

#hexa decimal=contain value between 0 to 9 or a to f (capital or small letter).(base 16)

d=0x12ade
print(d) #76510

#hex()=Return the hexadecimal representation of an integer.converts decimal number in hexa decimal.
n=12
print(hex(n)) #0xc

b=88
print(hex(b)) #0x58

s=15
print(hex(s)) #0xf

priti=30
print(hex(priti)) #0xle

# real part can be int or float.
c=10+5j #int
d=10.0+5j #float
k=0b1010+5j #binary
g=0o12+5j #octal
t=0xa+5j #hexa decimal
print(c,d,k,g,t)

#imag. part must be decimal or float.
c=5+10j #decimal
h=5+10.0j #float
print(c,h)




