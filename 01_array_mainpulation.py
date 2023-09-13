'''
1) You are given an array of integers a. 
A new array b is generated by rearranging the elements of a in the following way:
•	b[0] is equal to a[0];
•	b[1] is equal to the last element of a; b[2] is equal to a[1]; b[3] is equal to the second-last element of a; 
•	b[4] is equal to a[2]; 
•	b[5] is equal to the third-last element of a;
•	and so on. 
Your task is to determine whether the new array b is sorted in strictly ascending order or not.

'''


def array_manipulation(a):
    print(f"a: {a} ")
    n = len(a)
    b = [0] * n
    print(f"b: {b} ")
    left = 0
    right = n - 1
    for i in range(n):
        if i % 2 == 0:
            b[i] = a[left]
            left += 1
            print(f"------------------ITERATION {i} - b: {b} ")
        else:
            b[i] = a[right]
            right -= 1
            print(f"------------------ITERATION {i} - b: {b} ")
    print(f"========================> FINAL - a: {a} ")
    print(f"========================> FINAL - b: {b} ")
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return print(f"###NOT ASCENDING ORDER### b: {b} ") #False
    return print(f"------------------------------------------------------------>>>>> !!!ASCENDING ORDER!!! b: {b} ") #True


a = [1, 2, 3, 4, 5]
array_manipulation(a)

print(f"-------------------------------------")
print()

array_manipulation(a = [2,6,9,7,4])

print(f"-------------------------------------")
print()


a = [10,1,6,8,9,11]
array_manipulation([10,1,6,8,9,11])
#print(f"a: {a} ")




