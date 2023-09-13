'''
Given an array of strings schedule that represents the schedule of bus arrival times and a string time that represents the current time, find out how many minutes ago the last bus left. If the first bus for the day has yet to leave, return -1.
Time is represented as a string in the form of HH:MM (in the 24-hour format). Bus departure times are sorted in chronological order.
Please assume that if a bus is scheduled to leave at the current time, it hasn't left yet.
Example
•	For schedule = ["12:30", "14:00", "19:55"] and time = "14:30", the output should be solution(schedule, time) = 30.
Explanation:
The current time is "14:30". The last bus left at "14:00", so the answer is 30 minutes ago.
•	For schedule = ["00:00", "14:00", "19:55"] and time = "00:00", the output should be solution(schedule, time) = -1.
Explanation:
No buses left before "00:00" (the bus scheduled to leave at "00:00" hasn't left yet), so the answer is -1.
•	For schedule = ["12:30", "14:00", "19:55"] and time = "14:00", the output should be solution(schedule, time) = 90.
Explanation:
The current time is "14:00". The last bus left at "12:30" (the bus scheduled to leave at "14:00" hasn't left yet), so the answer is 90 minutes ago.

Input/Output
•	[execution time limit] 4 seconds (py3)
•	[input] array.string schedule
An array of strings representing the bus departure times in HH:MM format.
Guaranteed constraints:
3 ≤ schedule.length ≤ 100.
•	[input] string time
The current time in HH:MM format.
•	[output] integer
The number of minutes between the current time and the time when the last bus has left, or -1 if there weren't any buses that left before the current time.

'''

def solution(schedule, time):
    current_time = [int(x) for x in time.split(':')]
    print(f"current time: {current_time}")
    for bus_time in reversed(schedule):
        bus_time = [int(x) for x in bus_time.split(':')]
        print(f"bus time: {bus_time}")
        if bus_time < current_time:
            return (current_time[0] - bus_time[0]) * 60 + current_time[1] - bus_time[1]
    return -1

schedule = ["12:30", "14:00", "19:55"]
time = "14:30"
print(solution(schedule, time))  # Output: 30

schedule = ["00:00", "14:00", "19:55"]
time = "00:00"
print(solution(schedule, time))  # Output: -1

schedule = ["12:30", "14:00", "19:55"]
time = "14:00"
print(solution(schedule, time))  # Output: 90
