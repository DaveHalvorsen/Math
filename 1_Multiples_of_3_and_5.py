# This is Project Euler Problem 1: Multiples of 3 and 5 solved in Python 3.6.3.
# The task is to find the sum of all the multiples of 3 or 5 below 1000.

# current_sum is the current total of the sums. It needs to be defined before being used. 
current_sum = 0
# This for loop runs a full cycle of 0 - 999. Note that 1000 will not be run.
for i in range(1000):
    # You'll see 5 #commented out print lines. Those were used for code testing initially. 
    #print("The current i is: " + str(i))
    # The modulo operator is used to find if the current i is divisible by 3 
    if i % 3 == 0: 
        #print(str(i) + " is divisible by " + str(3))
        # The current i (that was divisible) is added to the current_sum.
        current_sum = current_sum + i
        #print("The current sum is: " + str(current_sum))
    # The modulo operator is used to find if the current i is divisible by 3 
    elif i % 5 == 0:
        #print(str(i) + " is divisible by " + str(5))
        # The current i (that was divisible) is added to the current_sum.
        current_sum = current_sum + i
        #print("The current sum is: " + str(current_sum))
# This final print statement only prints out the grandtotal.
print("The current sum is: " + str(current_sum))
# The answer this program agrees with what others have reported (233,168)
