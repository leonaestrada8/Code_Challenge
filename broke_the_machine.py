'''
Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
solution(a, b) = false;
For a = 2 and b = 3, the output should be
solution(a, b) = true.
Input/Output

'''
def solution(a, b):
    return (b-a)%2 != 0 or (a > b)
'''
def solution(a, b):
    print(f"a: {a}")
    print(f"b: {b}")
    if a == b:
        print(f"Both numbers are already equal: {a}")
        return
#    if a > b:
#        a, b = b, a
    counter = 0
    while a != b:
        
        print(f"-------")
        a += 1
        b -= 1
        print(f"a: {a}")
        print(f"b: {b}")
        counter += 1
        if counter == 10:
            print("TRUE - Both numbers are in an infinite loop")
            return
    print(f"FALSE - NOT INFINITE LOOP: Both numbers have reached the same value: {a}")
'''


solution(3,1)
solution(10,0)
solution(2,6)
solution(2,3)