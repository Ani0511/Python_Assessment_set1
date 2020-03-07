# Write a program to find the biggest of 4 numbers.
# a) Read 4 numbers from user using Input statement.
# b) extend the above program to find the biggest of 5 numbers.


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if(a>b and a>c and a>d):
    print("Biggest number is: ", a)
if(b>a and b>c and b>d):
    print("Biggest number is: ", b)
if(c>b and c>a and c>d):
    print("Biggest number is: ", c)
if(d>b and d>c and d>a):
    print("Biggest number is: ", d)

e = int(input("Enter another number: "))

if(a>b and a>c and a>d and a>e):
    print("Biggest number is: ", a)
if(b>a and b>c and b>d and b>e):
    print("Biggest number is: ", b)
if(c>b and c>a and c>d and c>e):
    print("Biggest number is: ", c)
if(d>b and d>c and d>a and d>e):
    print("Biggest number is: ", d)
if(e>b and e>c and e>d and e>a):
    print("Biggest number is: ", e)