

'''
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

'''



import time

def find_special_numbers(max_p):
    start_time = time.time()

    for p in range(1, max_p+1):
        for n in range(1, 10**6):
            if n % 1 == 0:  # check if n is an integer
                num_string = str(n)
                k = sum(int(digit)**(p+i) for i, digit in enumerate(num_string))
                if k % n == 0:
                    constant = k / n
                    if n >= 10:
                        print(f"{n} --> {' + '.join(digit + '^' + str(p+i) for i, digit in enumerate(num_string))} = {k} = {n} * {constant}")
                    else:
                        print(f"-----------------------------------------------------------------------------------------------{n} --> {' + '.join(digit + '^' + str(p+i) for i, digit in enumerate(num_string))} = {k} = {n} * {constant}")
    end_time = time.time()
    time_calculation = end_time - start_time
    time_calculation = round (time_calculation, 2)
    print("########################################################################### Calculation time: ", time_calculation , "seconds")


'''
The first function, find_special_numbers, takes in a maximum value for p (power at the first digit) and iterates over all
values of p from 1 to the max_p value passed in. It then iterates over all values of n from 1 to 10^6
(1 million) and converts each value of n to a string so that it can be iterated over.
Then, it calculates k using a list comprehension that raises the digit to the power of (p+i)
and sums all of the values together.
If k is divisible by n, it calculates the constant value by dividing k by n and prints out the result
'''

def dig_pow(n,p):
    digits = [int(d) for d in str(n)]
    for p in range(1, 11):
        k = sum([d**(p+i) for i, d in enumerate(digits)])
        if k == n * p:
            return p
    return -1

'''
The second function, dig_pow, takes in a number, n, and a variable p.
It converts the number to a list of digits and then iterates over all values of p from 1 to 11.
Within the for loop, it calculates k using a list comprehension that raises the digit to the power of (p+i)
and sums all of the values together.
If k is equal to n * p, it returns the value of p.
If the for loop completes without finding a solution, it returns -1.
'''




while True:
    choice = input("Enter 1 to validate a number or 2 to search for examples: ")
    if choice not in ["1", "2"]:
        print("Invalid choice, please enter 1 or 2.")
        continue
    if choice == "1":
        n = int(input("Enter a positive integer: "))
        p = 50
        result = dig_pow(n, p)
        if result != -1:
            print(f"======================SOLUTION FOUND:[ {n} --> {n} = {n} * {result} ]===========================================")
        else:
            print("---------------------------------------------------------------------No solution found.")
    elif choice == "2":
        max_p = int(input("Enter the maximum value of power (at the first digit) to check for special numbers: "))
        find_special_numbers(max_p)
    break
