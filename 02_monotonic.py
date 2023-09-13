'''
You are given an array of integers arr. Your task is to determine whether each sequence of three elements in the array (arr[i], arr[i + 1], and arr[i + 2]) are monotonic. Three consecutive elements are monotonic if their values are in a strictly increasing or strictly descreasing order.

Return an array of integers of length arr.length - 2, where the ith element is equal to 1 if arr[i] < arr[i + 1] < arr[i + 2] or arr[i] > arr[i + 1] > arr[i + 2], and 0 otherwise.

Example
•	For arr = [1, 2, 1, -4, 5, 10], the output should be solution(arr) = [0, 1, 0, 1].
The returned array output should look as follows:
o	output[0] = 0 because arr[0], arr[1], and arr[2] are not monotonic (1 < 2 > 1).
o	output[1] = 1 because arr[1], arr[2], and arr[3] are monotonic (2 > 1 > -4).
o	output[2] = 0 because arr[2], arr[3], and arr[4] are not monotonic (1 > -4 < 5).
o	output[3] = 1 because arr[3], arr[4], and arr[5] are monotonic (-4 < 5 < 10).
•	For arr = [10, 10, 10, 10, 10], the output should be solution(arr) = [0, 0, 0].
Since all elements of arr have the same value, it is impossible for any sequence of three elements to be monotonic.

Input/Output
•	[execution time limit] 4 seconds (py3)
•	[input] array.integer arr
An array of integers.
Guaranteed constraints:
3 ≤ arr.length ≤ 1000,
-109 ≤ arr[i] ≤ 109.
•	[output] array.integer
Return an array of integers (with 0 representing a "no" and 1 representing a "yes"), where the ith element represents whether arr[i], arr[i + 1], and arr[i + 2] are monotonic.
'''

def monotonic(arr):
    n = len(arr)
    output = []
    for i in range(n-2):
        if (arr[i] < arr[i+1] < arr[i+2]) or (arr[i] > arr[i+1] > arr[i+2]):
            output.append(1)
            print(f" output: {output} ")
        else:
            output.append(0)
            print(f" output: {output} ")
    return output

arr = [10, 10, 10, 10, 10]

monotonic(arr)

print(f"------------------------------------------------------------------")
print(f"------------------------------------------------------------------")

arr = [1, 2, 1, -4, 5, 10]

monotonic(arr)

