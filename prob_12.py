# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.


mylist = input("Enter 10 numbers").split()

sum = 0
for i in mylist:
    sum = sum+int(i);

avg = sum/10;
print("Average is: ", avg)

print("Printing the numbers less than the average: ")
for i in mylist:
    if(int(i)<avg):
        print(int(i))

print("Printing the numbers more than the average: ")
for i in mylist:
    if(int(i)>avg):
        print(int(i))

print("Printing the numbers equal to the average: ")
for i in mylist:
    if(int(i)==avg):
        print(int(i))
