'''
Create python code to get an array and create another one only with number which are bigger than both neighbors. 
The first and last element should always enter the new array because they dont have 2 neighbors.
'''


arr = [1, 2, 3, 2, 4, 1, 5]


def neighbors (arr):
    result = []
    print(f"array inicial: {arr}")
    for i in range(len(arr)):
        if i == 0 or i == len(arr) -1:
            print(f"inicial/final: {arr[i]}")
            result.append(arr[i])
        elif arr[i-1] < arr[i] > arr[i+1]:
            result.append(arr[i])
            print(f"maior que vizinhos: {arr[i]}")
    return result    
    
new_arr2 = neighbors(arr)
print(f"{new_arr2}")

def neighbors_chatgpt(arr):
    result = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            result.append(arr[i])
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            result.append(arr[i])
    return result

arr = [1, 2, 3, 2, 4, 1, 5]
new_arr = neighbors_chatgpt(arr)
print(new_arr) # Output: [1, 3, 4, 5]


























def bigger_than_neighbors(arr):
    new_arr = [arr[0]]
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            new_arr.append(arr[i])
    new_arr.append(arr[-1])
    return new_arr


arr = [1, 2, 3, 2, 4, 1, 5]
new_arr = bigger_than_neighbors(arr)
print(f"{new_arr}")


