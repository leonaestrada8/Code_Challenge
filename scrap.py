def solution27(lastNumberOfDays):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    possibilities = set() # set cannot have duplicates
    for i in range(len(days)):
        if days[i] == lastNumberOfDays:
            possibilities.add(days[(i + 1) % len(days)]) # [% len(days)] is used to start over if days[i+1] > len(days)
            print(f"i = {i}")
            print(f"possibilities = {possibilities}")
            #var = (i + 1) % len(days)
            #var2 = 14 % 12
            #print(f"var = {var}")
            #print(f"var2 = {var2}")
    
    print(f"Last Month number of days = {lastNumberOfDays}")
    print(f"=============================================>Possibilities for next month card renewal (number of days) = {sorted(list(possibilities))}")
    return sorted(list(possibilities))

print("-----------------bus_pass")
print(solution27(30))
print("---------------------------------------------------")
print(solution27(31))
print("###################################################")
solution27(28)