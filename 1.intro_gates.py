
'''
#1: You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.

Input/Output
'''

def sum_of_digits(n):
    # Get the last digit of the number
    last_digit = n % 10
    # Get the first digit by integer division
    first_digit = n // 10
    # Return the sum of the two digits
    return (n % 10) + (n // 10)


print(sum_of_digits(29))

#2: Given an integer n, return the largest number that contains exactly n digits.

def solution(n):
    return int('9' * n)

print(solution(5))


'''
#3: n children have got m pieces of candy. They want to eat as much candy as they can,
but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy
will be eaten by all the children together. Individual pieces of candy cannot be split.'''

def candy(n, m):
    return (m - (m % n))

# Test cases
print(candy(3, 10)) # 9

#print(m % n)
#For example, if m is 10 and n is 3, then m % n will be 1. 
#This means that we cannot divide 10 pieces of candy evenly among 3 children, so 1 piece will be left over.
print(candy(4, 10)) # 8
print(candy(2, 7)) # 6

'''
#4: Given the total number of rows and columns in the theater (nRows and nCols, respectively), 
and the row and column you're sitting in, return the number of people who sit strictly behind you
and in your column or to the left, assuming all seats are occupied.'''


def seats_in_theater(nRows, nCols, row, col):
    return (nRows - row) * (nCols - col + 1)


print(seats_in_theater(11, 16, 3, 5))

'''
#5: Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
solution(divisor, bound) = 9.

The largest integer divisible by 3 and not larger than 10 is 9.
'''

def find_divisor(divisor, bound):
    largest_divisible_integer = bound // divisor
    result = largest_divisible_integer * divisor
    print(f"The largest integer divisible by {divisor} and not larger than {bound} is {result}.")
    return result

#The // operator performs integer division, which returns the floor of the division result.

print(find_divisor(3, 10))

'''
6#: Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.
'''

def solution(n, firstNumber):
    return (firstNumber + n // 2) % n

'''

The n // 2 represents half of n, as we need to find the number that is diametrically opposite to firstNumber. 
By adding n // 2 to firstNumber, we get the number that is located n // 2 positions away from firstNumber.

The result is then taken modulo n to handle cases when the result is greater than n. 
This ensures that the returned result is always a valid number in the range from 0 to n - 1.
'''
def find_opposition(n, firstNumber):
    initial = (firstNumber + n // 2)
    valid = initial % n
    print(f"initial: {initial} adjustment: {valid}")
    print(f"Initial Position: {firstNumber} total positions: {n}, opposite position {valid}")
    return valid

print(find_opposition(9, 6))
print(find_opposition(8, 5))
print(find_opposition(17, 6))


print(find_opposition(4, 7))

'''
#7: One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.

When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

Example

For n = 240, the output should be
solution(n) = 4.

Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

For n = 808, the output should be
solution(n) = 14.

808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
'''

def conta_mins_bike(n):
    hours = n // 60
    minutes = n % 60
    #time = str(hours).zfill(2) + str(minutes).zfill(2)
    time = str(hours) + str(minutes)
    #time_clock = str(hours).zfill(2) + ":" + str(minutes).zfill(2)
    time_clock = str(hours) + ":" + str(minutes)
    print(time_clock)
    total = sum([int(i) for i in time])
    return total

print(conta_mins_bike(55))

'''
#8: Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?

Example

For min1 = 3, min2_10 = 1, min11 = 2, and s = 20, the output should be
solution(min1, min2_10, min11, s) = 14.

Here's why:

the first minute costs 3 cents, which leaves you with 20 - 3 = 17 cents;
the total cost of minutes 2 through 10 is 1 * 9 = 9, so you can talk 9 more minutes and still have 17 - 9 = 8 cents;
each next minute costs 2 cents, which means that you can talk 8 / 2 = 4 more minutes.
Thus, the longest call you can make is 1 + 9 + 4 = 14 minutes long.
'''

def solution4(min1, min2_10, min11, saldo):
    if saldo < min1:
        print(f"No Balance: {saldo}")
        return 0
    saldo -= min1
    print(f"Saldo após primeiro minuto: {saldo}")
    if saldo < 9 * min2_10:
        medium = 1 + (saldo // min2_10)
        print(f"Medium balance")
        print(f"saldo: {saldo} minutos: {medium}")
        print(f">> TOTAL DE MINUTOS: {medium}")
        return medium
    saldo -= 9 * min2_10
    high = 10 + (saldo // min11)
    print(f"High balance")
    print(f" saldo após 10 minutos: {saldo} \n TOTAL DE MINUTOS: {high}")
    return high

print(solution4 (3, 1, 2, 20))

'''
The solution involves a few steps to determine the maximum call duration based on the available balance and the cost per minute of the call. 
Here's a detailed explanation of the code:

1.First, we initialize four variables: min1, min2_10, min11, and s which represent the cost per minute of the first minute,
the cost per minute of minutes 2 through 10, the cost per minute of each minute after 10, and the available balance in cents, respectively.

2. Next, we calculate the maximum number of minutes the first minute can be used by subtracting the cost of the first minute (min1)
from the available balance (s). The result is stored in a variable duration.

3. Then, we subtract the cost of the first minute (min1) from the available balance (s) and store the result in balance.

4. After that, we calculate the maximum number of minutes for the minutes 2 through 10 (inclusive) by dividing the balance by the cost per minute (min2_10).
The result is stored in a variable minutes2to10.

5. To find the remaining balance after the minutes 2 through 10, we subtract the cost of these minutes from the balance and store the result in balance.

6. Finally, we calculate the maximum number of minutes after the 10th minute by dividing the remaining balance by the cost per minute of each minute after 10 (min11).
The result is stored in a variable minutesAfter10.

7. The total duration of the call is the sum of the minutes used in the first minute, minutes 2 through 10, and minutes after 10. This is stored in a variable duration.

8. Finally, we return the duration as the result of the function.

'''



