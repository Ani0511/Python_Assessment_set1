# Write a program to find the number is Prime or not.

a = 37
c = 0

if(a==0 or a==1):
    print("The number is not Prime.")
else:
    for i in range(2,a):
        if(a%i == 0):
            c += 1

    if(c == 0):
        print("The number is Prime.")
    else:
        print("The number is not Prime.")