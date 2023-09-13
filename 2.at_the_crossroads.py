
'''
#9: You are playing an RPG game. Currently your experience points (XP) total is equal to experience. 
To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, 
you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.

Example

For experience = 10, threshold = 15, and reward = 5, the output should be
solution(experience, threshold, reward) = true;
For experience = 10, threshold = 15, and reward = 4, the output should be
solution(experience, threshold, reward) = false.
'''


def solution5(experience, threshold, reward):
    new_exp = experience + reward
    if new_exp >= threshold:
        return True
    else:
        return False

def solution6(experience, threshold, reward):
    return experience + reward >= threshold

'''
#10: You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
solution(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
solution(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
solution(value1, weight1, value2, weight2, maxW) = 7.

You can't take both items, but you can take any of them.


'''

def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW and (value1 > value2 or weight2 > maxW):
        return value1
    elif weight2 <= maxW and (value2 >= value1):
        return value2
    else:
        return 0
    
'''
#11: You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?

Example

For a = 2, b = 7, and c = 2, the output should be
solution(a, b, c) = 7.

The two equal numbers are a and c. The third number (b) equals 7, which is the answer

'''
def solution8(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a
    

print(solution8(2,7,2))


'''
#12: Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
solution(a, b) = false;
For a = 2 and b = 3, the output should be
solution(a, b) = true.
'''
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def solution99(a, b):
    if (a > b) or ((b-a)%2 != 0):
        return True
    else:
        return False

solution99(2,6)
solution99(2,6)


def solution9(a, b):
    if a < b:
        diff = b - a
        print(diff)
        if diff < 2:
            diff *= 100
            print(diff)
        return (diff) % 2 == 0
    else:
        diff = a - b
        print(diff)
        if diff < 2:
            diff *= 100
            print(diff)
        return (diff) % 2 == 0
    
print(solution9(2,6))
print(solution9(2,3))

'''
#13: Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.

Example

For a = 2, b = 3, and c = 5, the output should be
solution(a, b, c) = true.

We can replace # with a + to obtain 2 + 3 = 5, so the answer is true.

For a = 8, b = 2, and c = 4, the output should be
solution(a, b, c) = true.

We can replace # with a / to obtain 8 / 2 = 4, so the answer is true.

For a = 8, b = 3, and c = 2, the output should be
solution(a, b, c) = false.

8 + 3 = 11 ≠ 2;
8 - 3 = 5 ≠ 2;
8 * 3 = 24 ≠ 2;
8 / 3 = 2.(6) ≠ 2.
So the answer is false.
'''

def solution10(a, b, c):
    add = a + b == c
    sub = a - b == c
    mul = a * b == c
    div = False if b == 0 else a / b == c

    if add or sub or mul or div:
        print(f"TRUE - Successful equations:")
        if add:
            print(f"{a} + {b} = {c}")
        if sub:
            print(f"{a} - {b} = {c}")
        if mul:
            print(f"{a} * {b} = {c}")
        if div:
            print(f"{a} / {b} = {c}")
        return True
    else:
        print(f"FALSE: NO succesful equations:")
        return False
    
def solution11(a, b, c):
    return c in (a+b,a-b,a*b,a/b)
    
def solution12(a, b, c):
    return a + b == c or a - b == c or a * b == c or a / b == c if b != 0 else False    

def solution13(a, b, c):
    if c in (a + b, a - b, a * b, a / b):
        operations = {a + b: f"{a} + {b}", a - b: f"{a} - {b}", a * b: f"{a} * {b}", a / b: f"{a} / {b}"}
        print(f"Successful equation: {operations[c]} = {c}")
        return True
    else:
        return False




print('equation_check')
print(solution10(2, 3, 5))
print("------------------------------")
print(solution11(2, 3, 5))
print("------------------------------")
print(solution12(2, 3, 5))
print("------------------------------")
print(solution13(2, 3, 5))
print("------------------------------")
print("------------------------------")
print(solution10(8, 2, 4))
print("------------------------------")
print(solution11(8, 2, 4))
print("------------------------------")
print("------------------------------")
print(solution10(8, 3, 2))
print("------------------------------")
print(solution11(8, 3, 2))

'''
#14: In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared the winner unless their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.

Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.

Example

For score1 = 3 and score2 = 6, the output should be
solution(score1, score2) = true.

Since player 1 hadn't reached 5 wins, the set ends once player 2 has won 6 games.

For score1 = 8 and score2 = 5, the output should be
solution(score1, score2) = false.

Since both players won at least 5 games, the set would've ended once one of them won the 7th one.

For score1 = 6 and score2 = 5, the output should be
solution(score1, score2) = false.

This set will continue until one of these players wins their 7th game, so this can't be the final score.
'''
def solution20(score1, score2):
    if (score1 < 7 and score2 < 7) or (abs(score1 - score2) < 2):
        print('1')
        return False
    if (score1 >= 6) and (score2 >= 4) or (score2 >= 6) and (score1 >= 4):
        print('2')
        return False
    if (score1 >= 6) and (score2 < 5) or (score2 >= 6) and (score1 < 5):
        print('3')
        return True
    return True


def solution21(score1, score2):
    mins, maxs = (min(score1, score2), max(score1, score2))
    return (maxs == 6 and mins < 5) or (maxs == 7 and mins in (5,6))


def solution22(score1, score2):
    mins =  min(score1, score2)
    maxs = max(score1, score2)
    if (maxs == 6 and mins < 5):
        return True
    if (maxs == 7 and mins in (5,6)):
        return True
    return False



print("------------------------------------tennis")
print(solution20(6, 4))
print(solution21(6, 4))
print(solution22(6, 4))

print(solution20(6, 2))
print(solution21(6, 2))
print(solution22(6, 2))


'''
#15: Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

they are young and beautiful but not loved;
they are loved but not young or not beautiful.
Example

For young = true, beautiful = true, and loved = true, the output should be
solution(young, beautiful, loved) = false.

Young and beautiful people are loved according to Mary's belief.

For young = true, beautiful = false, and loved = true, the output should be
solution(young, beautiful, loved) = true.

Mary doesn't believe that not beautiful people can be loved.
'''

def solution25(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    if loved and (not young or not beautiful):
        return True
    return False

def solution26(young, beautiful, loved):
    return loved != (young and beautiful)

'''
#16>:You just bought a public transit card that allows you to ride the Metro for a certain number of days.

Here is how it works: upon first receiving the card, the system allocates you a 31-day pass, which equals the number of days in January.
The second time you pay for the card, your pass is extended by 28 days, i.e. the number of days in February (note that leap years are not considered), and so on. 
The 13th time you extend the pass, you get 31 days again.

You just ran out of days on the card, and unfortunately you've forgotten how many times your pass has been extended so far. 
However, you do remember the number of days you were able to ride the Metro during this most recent month. 
Figure out the number of days by which your pass will now be extended, and return all the options as an array sorted in increasing order.

Example

For lastNumberOfDays = 30, the output should be
solution(lastNumberOfDays) = [31].

There are 30 days in April, June, September and November, so the next months to consider are May, July, October or December. 
All of them have exactly 31 days, which means that you will definitely get a 31-days pass the next time you extend your card.
'''

def solution27(lastNumberOfDays):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    possibilities = set() # set cannot have duplicates
    for i in range(len(days)):
        if days[i] == lastNumberOfDays:
            possibilities.add(days[(i + 1) % len(days)]) # [% len(days)] is used to start over if days[i+1] > len(days)
            print(f"i = {i}")
            print(f"possibilities = {possibilities}")
            #var = (i + 1) % len(days)
            #var2 = 14 % 12
            #print(f"var = {var}")
            #print(f"var2 = {var2}")
    
    print(f"Last Month number of days = {lastNumberOfDays}")
    print(f"Possibilities for next month card renewal (number of days) = {sorted(list(possibilities))}")
    return sorted(list(possibilities))

print("-----------------bus_pass")
print(solution27(30))
print("---------------------------------------------------")
print(solution27(31))
print("###################################################")
print(solution27(28))



