'''
#25: Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
solution(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
'''


def solution25(n):
    m = 1
    factorial = 1
    while factorial < n:
        m += 1
        factorial *= m
    return factorial

'''
In each iteration of the loop, the value of "m" is increased by 1 and the value of "factorial" is updated to be "factorial * m". 
The loop continues until "factorial" becomes greater than or equal to n.

The loop body essentially calculates the factorial of each integer starting from 1, 
and continues until it finds the smallest factorial that is not less than n. The final value of "m" is then returned as the answer.

0 ->	1
1 ->	1
2 ->	2
3 ->	6
4 ->	24
5 ->	120
6 ->	720


'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))

def solution33(n):
    m = factorial = 1
    #factorial = 1
    while factorial < n:
        m += 1
        factorial *= m
    return factorial

def solution34(n):
    f=i=1
    while f<n:
        f*=i
        i+=1
    return f

print(solution33(17))
print(solution34(17))

'''
The while loop in the code is used to find the smallest factorial (k) that is greater than or equal to the given integer n. 
The variable "m" is used as the counter and its value is initially set to 1. The variable "factorial" is used to store the value of m!.

In each iteration of the loop, the value of "m" is increased by 1 and the value of "factorial" is updated to be "factorial * m".
The loop continues until "factorial" becomes greater than or equal to n.

The loop body essentially calculates the factorial of each integer starting from 1, 
and continues until it finds the smallest factorial that is not less than n. The final value of "m" is then returned as the answer.
'''
##########################################################################################################################################
'''
#26: Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
solution(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
'''

def solution26(n, l, r):
    count = 0
    for a in range(l, r + 1):
        b = n - a
        if l <= b <= r and a <= b:
            count += 1
            print(f" {a} + {b} = {n}") 
    return count

'''
The code is looping through the range l to r inclusive. For each iteration, the value of a is determined and b is calculated as the difference between n and a. 
The value of b represents the second integer that is being added to a to sum up to n. 
The purpose of this loop is to find all possible combinations of a and b that satisfy the condition l ≤ A ≤ B ≤ r and count the number of such combinations.
'''


def solution26b(n, l, r):
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)


'''
The line b = n - a sets the value of b to be equal to n minus a. 
This is based on the requirement that n must be represented as the sum of two integers A and B, such that A + B = n. 
Since a is one of the integers, the other integer b can be found by subtracting a from n.
'''

print(f" {solution26(6, 2, 4)} solutions")
print(f" {solution26b(6, 2, 4)} solutions(fast)")

##############################################################################################

'''
#27: You are standing at a magical well. It has two positive integers written on it: a and b.
Each time you cast a magic marble into the well, it gives you a * b dollars and then both a and b increase by 1. 
You have n magic marbles. How much money will you make?

Example

For a = 1, b = 2, and n = 2, the output should be
solution(a, b, n) = 8.

You will cast your first marble and get $2, after which the numbers will become 2 and 3. When you cast your second marble, the well will give you $6.
Overall, you'll make $8. So, the output is 8.
'''

def solution27(a, b, n):
    result = 0
    for i in range(n):
        result += a * b
        a += 1
        b += 1
    return result

def solution27b(a, b, n):
    return sum([(a + i) * (b + i) for i in range(n)])


print(solution27(1, 2, 2))
print(solution27b(1, 2, 2))


'''
#28: To prepare his students for an upcoming game, the sports coach decides to try some new training drills. 
To begin with, he lines them up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. 
Alternatively, when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around.

Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when they hear 'R'.
The coach wants to know how many times the students end up facing the same direction.

Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.

Example

For commands = "LLARL", the output should be
solution(commands) = 3.

Let's say that there are 4 students, and the second one can't tell left from right. 
In this case, only after the second, third and fifth commands will the students face the same direction.
'''



def solution28(commands):
    count = 0
    direction = 0
    check = False
    
    for i in range(len(commands)):
        c = commands[i]
        print(commands[i])
        if c == 'L':
            direction -= 90
            print(direction)
        elif c == 'R':
            direction += 90
            print(direction)
        elif c == 'A':
            direction += 180
            print(direction)
        var = direction % 180
        if var == 0:
            count += 1
            print(f"count: {count}")
            check = True
        elif check and c == 'A':
            count += 1
            print(f"count: {count}")
        else:
            check = False
    
    return count




print(solution28(commands="LLARL"))


'''
#29: Given two integers, your task is to find the result of addition without carrying

Example

For param1 = 456 and param2 = 1734, the output should be
solution(param1, param2) = 1180.

   456
  1734
+ ____
  1180

the following operations from right to left will be performed:

6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.
'''


def solution29(param1, param2):
    result = 0
    factor = 1
    while param1 > 0 or param2 > 0:
        print(f"PARAM1: {param1}")
        print(f"PARAM2: {param2}")
        print(f"FACTOR: {factor}")
        result += factor * ((param1 % 10 + param2 % 10) % 10)
        print(f"-------result: {result}")
        param1 //= 10
        param2 //= 10
        factor *= 10
    return result

def solution29b(param1, param2):
    result = 0
    tenPower = 1
    while param1 > 0 or param2 > 0:
        result += tenPower * ((param1 + param2) % 10)
        param1 //= 10
        param2 //= 10
        tenPower *= 10
    return result

print(solution29(456, 1734))
print(solution29b(456, 1734))




'''
#30: You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

The smallest box is size 1, the next one is size 2,..., all the way up to size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.

Example

For k = 5, the output should be
solution(k) = -15.

There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.
'''

def solution39(k):
    odd = 0
    even = 0
    for i in range(k+1):
        if i % 2 != 0:
            qtd = i * i
            odd += qtd
            print(f"--------------ODD: {qtd}")
        else:
            qtd = i * i
            even += qtd
            print(f"--------------EVEN: {qtd}")
    total = odd + even
    diff = even - odd
    print(f"Number of Boxes: {k}")
    print(f"Number of Yellow apples (odd): {odd}")       
    print(f"Number of Yellow apples (even): {even}")       
    print(f"TOTAL NUMBER OF APPLES: {total}")       
    print(f"DIFF RED - YELLOW: {diff}")       
    return diff

def solution40(k):
    yellow_apples = 0
    red_apples = 0
    for i in range(1, k + 1):
        if i % 2 == 1:
            yellow_apples += i * i
        else:
            red_apples += i * i
    return red_apples - yellow_apples


solution39(5)
solution40(5)

'''
#31: Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
solution(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
solution(n) = false.

Roundness of n is 3, and there is no way to increase it.
'''



def solution31(n):
    roundness = len(str(n)) - len(str(n).rstrip('0'))
    for i in range(len(str(n))):
        for j in range(i + 1, len(str(n))):
            if str(n)[i] == '0' and str(n)[j] != '0':
                n = int(str(n)[:i] + str(n)[j] + str(n)[i+1:j] + str(n)[i] + str(n)[j+1:])
                if len(str(n)) - len(str(n).rstrip('0')) > roundness:
                    return True
    return False

print(solution31(902200100))
print(solution31(11000))


'''
#32: We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach.
# This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10.
# If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1).
# The process stops immediately once there is only one non-zero digit left.

Example

For n = 15, the output should be
solution(n) = 20;

For n = 1234, the output should be
solution(n) = 1000.

1234 -> 1230 -> 1200 -> 1000.

For n = 1445, the output should be
solution(n) = 2000.

1445 -> 1450 -> 1500 -> 2000.
'''














'''
#33: When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?

Example

For candlesNumber = 5 and makeNew = 2, the output should be
solution(candlesNumber, makeNew) = 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.
'''
def solution33(candlesNumber, makeNew):
    total_burned = candlesNumber
    leftovers = candlesNumber
    while leftovers >= makeNew:
        new_candles = leftovers // makeNew
        leftovers = (leftovers % makeNew) + new_candles
        total_burned += new_candles
    return total_burned



print(solution33(5,2))