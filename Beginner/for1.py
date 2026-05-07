'''1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20times). Count and print the following 
statistics: 
How many times you rolled a 6 
How many times you rolled a 1 
How many times you rolled two 6s in a row'''

import random

roll=20
count_1=0
count_6=0
result=[]
two6=0
prev_6=False

for i in range(0,roll+1):
    roll=random.randint(1,6)
    result.append(roll)
    print(f"Roll {i}:",roll)
    if roll==6:
        count_6+=1
        if prev_6:
            two6+=1
        prev_6=True
    else:
        prev_6=False
    if roll==1:
        count_1+=1
print("Number of times 6 apperead: ",count_6)
print("Number of times 1 apperead: ",count_1)
print("Number of times two 6 apperead: ",two6)