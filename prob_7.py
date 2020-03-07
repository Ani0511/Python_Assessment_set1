# Create a list with at least 10 elements having integer values in it;
# Print all elements
# Perform slicing operations
# Perform repetition with * operator
# Perform concatenation with other list.


mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(mylist)

for i in mylist:
    print(i)

print(mylist[2:6])

print(mylist*2)

mylist2 = [1, 2, 3, 4, 5]

mylist3 = mylist + mylist2
print(mylist3)