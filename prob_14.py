# Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
#     a) Print all names on to screen
#     b) Read the index from the  user and print the corresponding name from both list.
#     c) Print the names from 4th position to 9th position
#     d) Print all names from 3rd position till end of the list
#     e) Repeat list elements by specified number of times (N- times, where N is entered by user)
#     f)  Concatenate two lists and print the output.
#     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )


A = input("Enter Employee IDs: ").split()
B = input("Enter Employee Names: ").split()

print("------------------------------------------------")
# operation (a)
print("All the names are: ")
for i in B:
    print(i)

print("------------------------------------------------")
# operation (b)
a = int(input("Enter the index value: "))
print("Respective Employee ID is: ", A[a])
print("Respective Employee Name is: ", B[a])

print("------------------------------------------------")
# operation (c)
for i in range(4, 10):
    print(B[i])

print("------------------------------------------------")
# operation (d)
for i in B[3:]:
    print(i)

print("------------------------------------------------")
# operation (e)
x = int(input("How many times you want to print: "))
print(A*x)
print(B*x)

print("------------------------------------------------")
# operation (f)
print(A+B)

print("------------------------------------------------")
# operation (g)
print(A,B)


