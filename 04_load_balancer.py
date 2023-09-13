'''
Imagine that you are implementing a simplified load balancer to route user requests to multiple servers. You are given an array of integers serversPowers,
where serversPowers[i] (assume 0-based indexing) is an integer between 1 to 5 representing the capacity of the ith server -
the maximum number of user requests that the server can handle during each cycle. You are also given an array of strings events, 
where events[i] can be one of the following:
•	"REQUEST" - user request
•	"FAIL <i>" - shut down the ith server, so it can no longer serve any requests
The load balancer handles user requests by routing them to the servers in cyclic order - each server should serve as many requests as it can be based on its total capacity defined by serversPowers[i] before requests are routed to the next server (i.e., the i+1th server). After each cycle (i.e., when requests must be routed to serversPowers[0] again), the capacity of all non-failed servers is reset, but failed servers should remain shut down/inactive.
Notes
•	The load balancer should bypass any servers which are failed/shut down when routing requests.
•	It is guaranteed that there is at least one functioning server at all times.
Return the index of the server that has served most of the requests, or in case of a tie, return the server with the largest index.
Note: Failed servers should be considered.
Example
For serversPowers = [1, 2, 1, 2, 1] and

events = [
  "REQUEST",
  "REQUEST",
  "FAIL 2",
  "REQUEST",
  "FAIL 3",
  "REQUEST",
  "REQUEST"
]
the output should be solution(serversPowers, events) = 1.
Explanation:
•	events[0] = "REQUEST" – the first request goes to server 0, so the requests count for each server is [1, 0, 0, 0, 0] and left capacities are [0, 2, 1, 2, 1],
•	events[1] = "REQUEST" – as the server with index 0 has reached its maximum capacity, this request goes to server 1, so the requests count for each server is [1, 1, 0, 0, 0] and left capacities are [0, 1, 1, 2, 1] now,
•	events[2] = "FAIL 2" – the server with index 2 is shut down,
•	events[3] = "REQUEST" – this request goes to server 1 as it still has the capacity, so the requests count for each server is [1, 2, 0, 0, 0] and left capacities are [0, 0, 1, 2, 1] now,
•	events[4] = "FAIL 3" – the server with index 3 is shut down,
•	events[5] = "REQUEST" – this request goes to server 4, bypassing servers with index 2 and 3 as those are shut down, so the requests count for each server is [1, 2, 0, 0, 1] and left capacities are [0, 0, 1, 2, 0] now,
•	As the last server has reached its maximum capacity, the next server to check is the server 0 again following the cyclic order, so all servers' capacities are reset. The left capacities are [1, 2, 1, 2, 1] now,
•	events[6] = "REQUEST" – this request goes to server 0, so the requests count for each server is [2, 2, 0, 0, 1] and left capacities are [0, 2, 1, 2, 1] now,
•	Thus, the number of requests served by each server is [2, 2, 0, 0, 1]. Since both servers 0 and 1 have served the most requests at 2 each, the final answer is the largest index of 1.
Input/Output
•	[execution time limit] 4 seconds (py3)
•	[input] array.integer serversPowers
An array of integers representing the capacity of the servers to which requests should be routed.
Guaranteed constraints:
1 ≤ serversPowers.length ≤ 100,
1 ≤ serversPowers[i] ≤ 5.
•	[input] array.string events
An array of events to be processed by the load balancer.
Guaranteed constraints:
1 ≤ events.length ≤ 1000.
•	[output] integer
The index of the server which served the highest number of requests. If multiple servers can tie for the highest number of requests, return the largest index among these servers.

'''

def solution(serversPowers, events):
    n = len(serversPowers)
    counters = [0] * n
    failed = set()
    max_requests = 0
    max_index = -1
    next_server = 0
    for event in events:
        if event == "REQUEST":
            while next_server in failed or serversPowers[next_server] <= counters[next_server]:
                next_server = (next_server + 1) % n
            counters[next_server] += 1
            if counters[next_server] > max_requests:
                max_requests = counters[next_server]
                max_index = next_server
        else: # event == "FAIL i"
            i = int(event.split()[1])
            failed.add(i)
            if i == max_index:
                max_requests = 0
                max_index = -1
    return max_index

serversPowers = [1, 2, 1, 2, 1] 
events = [
  "REQUEST",
  "REQUEST",
  "FAIL 2",
  "REQUEST",
  "FAIL 3",
  "REQUEST",
  "REQUEST"
]

solution(serversPowers, events)