# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop 
# b) By using while loop
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.


for i in range(1,101):
    print(i)

for i in range(100, 0, -1):
    print(i)

j = 1
while(j<=100):
    print(j)
    j += 1

j = 100
while(j>=1):
    print(j)
    j -= 1

mystring = "Hello world"
for x in mystring:
    print(x)