'''
#17: Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. 
The message contains several numbers that, when typed into a supercomputer, 
will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. 
More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. 
It's now up to you to write a function that will change the kth bit of n back to 0.
'''

print("-----------------spy_code")


def solution30(n, k):
    mask = 1 << (k - 1)
    
    print(f"mask= {mask}")
    result = n & ~mask
    print(f"n = {n}")
    print(f"mask bin   = {bin(mask)}")
    print(f"~ mask bin   = {bin(~mask)}")
    print(f"n bin      = {bin(n)}")
    print(f"result bin = {bin(result)}")
    print(f"result = {result}")
    return result

'''
The line mask = 1 << (k - 1) creates a binary number with a 1 in the k-th position from the right, and all other bits set to 0.

The 1 represents a binary number with the least significant bit set to 1. The << (k - 1) operator shifts the 1 to the left by k - 1 positions, 
effectively moving it to the k-th position from the right.

For example, if k = 3, the expression 1 << (k - 1) evaluates to 1 << (3 - 1), which is 1 << 2. The binary representation of 1 << 2 is 100, 
which has a 1 in the third position from the right.

'''

def solution31(n, k):
    return n & ~(1 << (k - 1))

print (solution30(37,5))
print (solution31(37,5))
print (solution30(2147483647,16))
print (solution31(2147483647,16))


'''
#18: You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. For further clarification see the following example.

Example

For a = [24, 85, 0], the output should be
solution(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience), which equals to 21784.
'''

arr = [24, 85, 0]

def solution32(a, b, c):
    #arr = [24, 85, 0]
    arr = [a, b, c]
    var1 = bin(arr[1])
    var2 = bin(arr[2])
    var3 = bin(arr[3])
    total = str(var1) + str(var2) + str(var3)
    final = int(total)
    return final


