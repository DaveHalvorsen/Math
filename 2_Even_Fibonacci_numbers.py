# This is a Python 3.6 solution to Project Euler question 2: Even Fibonacci numbers.
# Find the sum of the even terms of the Fibonacci sequence that do not exceed 4M.
# 4 million is 4 X 10^6 

current_sum = 0
last_Fibonacci = 0
current_Fibonacci = 1
while current_Fibonacci <= 4000000:
    print("Current Fibonacci is: " + str(current_Fibonacci))
    if current_Fibonacci % 2 == 0:
        print(str(current_Fibonacci) + " is an even number")
        current_sum = current_sum + current_Fibonacci
        print("Current sum is: " + str(current_sum))

    placeholder_Fibonacci = current_Fibonacci
    current_Fibonacci = current_Fibonacci + last_Fibonacci
    last_Fibonacci = placeholder_Fibonacci
print("Final sum is: " + str(current_sum)) 

