# Write program to find the biggest and Smallest of N numbers.
# PS: Use the functions to find biggest and smallest numbers. 


n = int(input("How many numbers are there: "))

mylist = input("Enter the numbers: ").split()

def small(mylist):
    s = int(mylist[0])
    for i in mylist:
        if(int(i)<s):
            s = int(i)
    return s

def big(mylist):
    b = int(mylist[0])
    for i in mylist:
        if(int(i)>b):
            b = int(i)
    return b

print("The smallest number is: ", small(mylist))
print("The biggest number is: ", big(mylist))

