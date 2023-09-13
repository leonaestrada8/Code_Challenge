

''''
aNTONIO CONSELHEIRO
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    r = min(255, max(0, r))
    g = min(255, max(0, g))
    b = min(255, max(0, b))
    return "{:02X}{:02X}{:02X}".format(r, g, b)
    
    
This function first checks if the values of r, g, and b are within the range of 0 to 255. If not, 
it rounds the value to the closest valid value by using the min and max functions. 
Then it returns the hexadecimal representation of the RGB values, 
formatted as a string with leading zeros to ensure that it is always 6 characters long.

---------------------------------------------------

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
'''


def create_phone_number(numbers):
    area_code = ''.join(map(str, numbers[:3]))
    prefix = ''.join(map(str, numbers[3:6]))
    line_number = ''.join(map(str, numbers[6:]))
    return f'({area_code}) {prefix}-{line_number}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))