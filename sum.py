

"""def get_sum(a, b):    SOLUTION ONE
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
    """

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
    
print(get_sum(1, 0))  # -1
print(get_sum(1, 2))  # 3
print(get_sum(0, 1))  # 1
