'''
4) You are given two arrays of integers a and b, and an array queries, the elements of which are queries you are required to process. Every queries[i] can have one of the following two forms:
•	[0, i, x]. In this case, you need to assign a[i] the value of x (a[i] = x).
•	[1, x]. In this case, you need to find the total number of pairs of indices i and j such that a[i] + b[j] = x.
Perform the given queries in order and return an array containing the results of the queries of the type [1, x].
Example
•	For a = [3, 4], b = [1, 2, 3], and queries = [[1, 5], [0, 0, 1], [1, 5]], the output should be solution(a, b, queries) = [2, 1].
The arrays look like this initially:
a = [3, 4] and b = [1, 2, 3]
For the query [1, 5], there are two ways to form a sum of 5 using an element from each array: 5 = 3 + 2 = a[0] + b[1] and 5 = 4 + 1 = a[1] + b[0]. So the result is 2.
The query [0, 0, 1] re-assigns the value of a[0] to 1, so the arrays now look like this:
a = [1, 4] and b = [1, 2, 3]
For the final [1, 5] query, there's now only one way to form a sum of 5 using an element from each array: 5 = 4 + 1 = a[1] + b[0]. So the result is 1.
Since the two queries of type [1, x] gave results of 2 and 1 respectively, the answer is [2, 1].

•	For a = [2, 3], b = [1, 2, 2], and queries = [[1, 4], [0, 0, 3], [1, 5]], the output should be solution(a, b, queries) = [3, 4].
The arrays look like this initially:
a = [2, 3] and b = [1, 2, 2]

For the query [1, 4], there are three ways to form a sum of 4 using an element from each array: 4 = 2 + 2 = a[0] + b[1], 4 = 2 + 2 = a[0] + b[2], and 4 = 3 + 1 = a[1] + b[0]. So the result is 3.

The query [0, 0, 3] re-assigns the value of a[0] to 3, so the arrays now look like this:

a = [3, 3] and b = [1, 2, 2]
For the query [1, 5], there are now 4 ways to form a sum of 5 using an element from each array: 5 = 3 + 2 = a[0] + b[1], 5 = 3 + 2 = a[0] + b[2], 5 = 3 + 2 = a[1] + b[1], and 5 = 3 + 2 = a[1] + b[2]. So the result is 4.
Since the two queries of type [1, x] gave results of 3 and 4 respectively, the answer is [3, 4].

Input/Output
•	[execution time limit] 4 seconds (py3)
•	[input] array.integer a
An array of integers.
Guaranteed constraints:
1 ≤ a.length ≤ 5 · 104,
0 ≤ a[i] ≤ 109.
•	[input] array.integer b
An array of integers.
Guaranteed constraints:
1 ≤ b.length ≤ 103,
0 ≤ b[i] ≤ 109.
•	[input] array.array.integer queries
An array of queries, where queries[i][0] represents the type of query, and the other elements represent the parameters of the query (i and x for type 0, and just x for type 1).
For queries of the type [0, i, x], it is guaranteed that 0 ≤ i < a.length and 0 ≤ x ≤ 109.
For queries of the type [1, x], it is guaranteed that 0 ≤ x ≤ 2 · 109
Guaranteed constraints:
1 ≤ queries.length ≤ 103.
•	[output] array.integer
The output of the queries of the type [1, x], in the order that they are given in the input.

'''

def solution(a, b, queries):
    
    # Create a dictionary 'pair_counts' to store the frequency count of each sum of pairs
    # between the elements of 'a' and 'b'.
    pair_counts = {}
    for i in range(len(a)):
        for j in range(len(b)):
            pair_sum = a[i] + b[j]
            # Add the sum of each pair to 'pair_counts', initializing its frequency count to 0
            if pair_sum not in pair_counts:
                pair_counts[pair_sum] = 0
            pair_counts[pair_sum] += 1
    
    # Initialize variables to keep track of the counts of pair sums before and after updates to a.
    before_count = sum(pair_counts.get(x[1], 0) for x in queries if x[0] == 1)
    after_count = before_count
    results = []
    
    # For each query in 'queries', perform the appropriate operation and update the counts of pair sums.
    for query in queries:
        # If the query is of the form [0, i, x], update a[i] to be x, and update 'pair_counts' with the new pairs
        if query[0] == 0:
            i, x = query[1:]
            old_a = a[i]
            a[i] = x
            for j in range(len(b)):
                old_pair_sum = old_a + b[j]
                if old_pair_sum in pair_counts:
                    pair_counts[old_pair_sum] -= 1
                new_pair_sum = x + b[j]
                if new_pair_sum not in pair_counts:
                    pair_counts[new_pair_sum] = 0
                pair_counts[new_pair_sum] += 1
            after_count = sum(pair_counts.get(x[1], 0) for x in queries if x[0] == 1)
        # If the query is of the form [1, x], find the frequency count of the sum x in 'pair_counts' and add it to 'results'
        elif query[0] == 1:
            x = query[1]
            results.append(pair_counts.get(x, 0))
    
    # Return the counts of pair sums before and after updates to a.
    return results


# Example inputs
a = [3, 4]
b = [1, 2, 3]
queries = [[1, 5], [0, 0, 1], [1, 5]]

# Call the function with the example inputs and print the output
print(solution(a, b, queries)) # Expected output [2, 1].
print('===============================================================')
print('===============================================================')
a = [2, 3]
b = [1, 2, 2]
queries = [[1, 4], [0, 0, 3], [1, 5]]
print(solution(a, b, queries)) # Expected output [3, 4].



