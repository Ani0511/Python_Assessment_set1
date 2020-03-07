# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# a) From the above statement your program should receive arguments and print them each of them. 
# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.


import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if(a>b and a>c):
    print("Biggest number is: ", a)
if(b>a and b>c):
    print("Biggest number is: ", b)
if(c>a and c>b):
    print("Biggest number is: ", c)