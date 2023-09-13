def find_odd_occurrence(arr):
    # Create an empty dictionary
    num_count = {}
    
    # Iterate through the array and count the number of occurrences of each number
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Iterate through the dictionary and return the numbers that have an odd number of occurrences
    odd_occurrences = []
    for num, count in num_count.items():
        if count % 2 != 0:
            odd_occurrences.append(num)
    
    return odd_occurrences


arr = [1, 2, 3, 2, 3, 1, 3, 1]
print(find_odd_occurrence(arr)) # Output: [3]
