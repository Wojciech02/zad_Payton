# Wojciech fuśnik

a=2
b=4
c=3

d = b*b - 4*a*c
if d<0:
    print("Delta mniejsza od zera")
elif d>0:
    print("Delta wieksza od zera")
else:
    print("Delta rowna zero")

l1 = input("system dwojkowy")
l2 = input("system osemkowy")
l3 = input("sysytem szesnastkowy")

print(bin(l1)[2:0])
print(oct(l2)[2:0])
print(hex(l3)[2:0])