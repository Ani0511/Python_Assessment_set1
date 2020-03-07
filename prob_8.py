# Create a tuple with at least 10 elements having integer values in it;
# Print all elements
# Perform slicing operations
# Perform repetition with * operator
# Perform concatenation with other tuple.


mytup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(mytup)

for i in mytup:
    print(i)

print(mytup[2:6])

print(mytup*2)

mytup2 = (1, 2, 3, 4, 5)

mytup3 = mytup + mytup2
print(mytup3)