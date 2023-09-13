'''Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''

def break_camel_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result

print(break_camel_case("camelCasing"))
print(break_camel_case("identifier"))
print(break_camel_case(""))

