def human_readable_time(num_seconds):
    hours = num_seconds // 3600
    minutes = (num_seconds % 3600) // 60
    seconds = num_seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


num_seconds = int(input("Enter a number of seconds for conversion: \n"))
print(human_readable_time(num_seconds))
