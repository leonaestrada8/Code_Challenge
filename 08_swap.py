'''
You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. 
If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).
Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.
Example
•	For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.
The initial array is already strictly increasing, so no actions are required.
•	For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.
By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.
•	For numbers = [13, 31, 30], the output should be solution(numbers) = false.
o	The initial array elements are not increasing.
o	By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
o	By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
o	By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
So, it's not possible to obtain a strictly increasing array, and the answer is false.
Input/Output
•	[execution time limit] 4 seconds (py3)
•	[input] array.integer numbers
An array of non-negative integers.
Guaranteed constraints:
1 ≤ numbers.length ≤ 103,
0 ≤ numbers[i] ≤ 103.
•	[output] boolean
Return true if it is possible to obtain a strictly increasing array by applying the digit-swap operation at most once, and false otherwise.

'''


numbers = [1, 5, 10, 20]




















def solutionb(numbers):
    if numbers == sorted(numbers):
        return True
    n = len(numbers)
    for i in range(n):
        s = str(numbers[i])
        for j in range(len(s)):
            for k in range(j+1, len(s)):
                if j == 0 and s[k] == '0':
                    continue  # skip leading zeros
                new_num = int(s[:j] + s[k] + s[j+1:k] + s[j] + s[k+1:])
                print(f"NEW ------: {new_num}")
                if new_num > numbers[i]:
                    new_numbers = numbers[:i] + [new_num] + numbers[i+1:]
                    print(f"ORIGINAL LIST: {numbers}")
                    print(f"NEW LIST: {new_numbers}")
                    if new_numbers == sorted(new_numbers):
                        return True
    return False



'''


numbers = [1, 5, 10, 20]
print(solution(numbers))
print("=================================================================")

#expected output = True because the initial array is already strictly increasing, so no actions are required.
#Real output = FALSE

numbers = [1, 3, 900, 10]
print(solution(numbers))
#expected output = the output should be solution(numbers) = true. By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

print("=================================================================")

numbers = [13, 31, 30]
print(solution(numbers))

'''
