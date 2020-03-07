# Create a list of 5 names and check given name exist in the List.
#        a) Use membership operator (IN) to check the presence of an element.
#        b) Perform above task without using membership operator.
#        c) Print the elements of the list in reverse direction.

mylist = ["Anirudhya", "Renesa", "Jayanta", "Srabani", "Gita"]

name =  input("Enter a name: ")

# operation (a)
if name in mylist:
    print("Present")
else:
    print("Not Present")

# operation (b)
for i in mylist:
    if(name == i):
        print("Present")
        break
    else:
        print("Not Present")

# operation (c)
for i in range(4,-1,-1):
    print(mylist[i])