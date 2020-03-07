# Using loop structures print even numbers between 1 to 100.  
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#    i) Break the loop if the value is 50
#    ii) Use continue for the values 10,20,30,40,50
# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#      i) Break the loop if the value is 90
#      ii) Use continue for the values 60,70,80,90


for i in range(2, 101, 2):
    if(i == 50):
        break
    if(i%10 == 0):
        continue
    else:
        print(i)

i = 1
while(i<=100):
    if(i==90):
        break
    if(i==60 or i==70 or i==80):
        i = i+1
        continue
    if(i%2 == 0):
        print(i)
    i = i+1