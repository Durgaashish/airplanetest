"""
There are 100 passengers about to board a plane with 100 seats.
Each passenger is assigned a distinct seat on the plane. The first passenger who boards has
forgotten his seat number and sits in a randomly selected seat on the plane. Each passenger who boards after him either
sits in his or her assigned seat if it is empty or sits in a randomly selected seat from the unoccupied seats.
What is the probability that the last passenger to board the plane sits in his/her assigned seat?








solution:

only if the seat is empty the following passenger sits in it
else a random seat

use for loop for iteration from 1 to 100
number 1 will be randomly assigned outside the loop

from second number we will use a random method and assign it in a random index from 1 to 100
while assigning check the matching index first if it is empty before assigning. if not empty assign a different index
when the loop ends every number is assigned to a number
we will then compare and check the last number is in the matching index or a different index.
----



"""
import random
numofseats=100
seats=[0]*numofseats
assign=[]
for a in range(len(seats)):
    assign.append(a) #storing index values in an array
p1=random.choice(assign) #selecting a random index to store passenger1 seat

seats[p1] = 1
for i in range(len(seats)):


    if(seats[i]==0 and i!=0 and i<numofseats):
        seats[i]=i+1
    else:
        del assign[1:i]#eliminating the assigned seats before randomly selecting a seat
        k = random.choice(assign) #storing a random index value
        if(seats[k]==0):

            seats[k] = i+1

if(numofseats!=1): #probability of 100th passenger gets 100th seat
   print("probability is",0.5)   #here every passenger except for passenger 1 has two choices to either sit in their seat or in a random seat which makes its probability 1/2
else:
    print("probability is",1)






