# Write a program to read string and print each character separately.
# a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
# b) Repeat the string 100 times using repeat operator *
# c) Read string 2 and concatenate with other string using + operator.

# for the general part
str = input("Enter a string: ")

for i in str:
    print(i)

# for the (a) part
substr = str[2:4]
print(substr)

# for the (b) part
print(str*10)

# for the (c) part 
str2 = input("Enter the second string: ")
print(str+str2)
