# Write program to perform following:
#     i) Check whether given number is prime or not.
#    ii) Generate all the prime numbers between 1 to N where N is given number.


a = int(input("Enter a number: "))

c = 0
for i in range(1,a+1):
    if(a%i == 0):
        c += 1
if(c == 2):
    print("Prime")
else:
    print("Not Prime")

b = int(input("Enter another number: "))

for j in range(1,b):
    d = 0
    for i in range(1, j+1):
        if(j%i == 0):
            d += 1
    if(d == 2):
        print(j)
    else:
        continue