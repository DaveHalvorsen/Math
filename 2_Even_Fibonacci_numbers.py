# This is a Python 3.6 solution to Project Euler question 2: Even Fibonacci numbers.
# Find the sum of the even terms of the Fibonacci sequence that do not exceed 4M.
# 4 million is 4 X 10^6 

# current_sum will store the sum of all the even Fibonacci #s processed
current_sum = 0
# last_Fibonacci will store the Fibonacci # from the last round and current_Fibonnaci
# stores the current #. I need to use both to always have access to the last # and the 
# current #.
last_Fibonacci = 1
current_Fibonacci = 1
# The problem specifies that we'll be summing the even numbers that 
# *do not exceed* 4X10^6. I'm using a while loop to keep the numbers under 4X10^6
while current_Fibonacci <= 4000000:
    # These print statements keep track of where we are with the last & current Fib #s
    print("Last Fibonacci is: " + str(last_Fibonacci))
    print("Current Fibonacci is: " + str(current_Fibonacci))
    # If the current Fib # is divisible by 2 (w/ the Modulo), then a print statement
    # notifies the user AND sums the even Fib # to the previous sum of the even 
    # Fib #s.
    if current_Fibonacci % 2 == 0:
        print(str(current_Fibonacci) + " is an even number")
        current_sum = current_sum + current_Fibonacci
        print("Current sum is: " + str(current_sum))
    # The next Fibonacci # is determined by summing the current # with the last #.
    # The current_Fibonacci # is saved in the placeholder variable (for later use).
    # The current_Fibonacci # is added to the last Fib # and then the last_Fib # 
    # is updated to the placeholder_Fibonacci #.
    placeholder_Fibonacci = current_Fibonacci
    current_Fibonacci = current_Fibonacci + last_Fibonacci
    last_Fibonacci = placeholder_Fibonacci
# Here, the final sum is printed.
print("Final sum is: " + str(current_sum)) 

