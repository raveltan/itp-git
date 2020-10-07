print("Random Number Generator")
import random
a = int(input("How many numbers? "))
ctr = 1
b,c = eval(input("What is your range, (separated with a comma)? "))
while(ctr <= a):
    num = random.randint(b,c)
    if(ctr > a):
        break
    ctr += 1
    print(num, end=" ")
