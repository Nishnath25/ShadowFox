'''1. Write a function that takes two arguments, 145 and 'o'
, and
uses the `format` function to return a formatted string. Print the
result. Try to identify the representation used.'''

def format_string(num,char):
    result=format(num,char)
    print(result)
    return result
format_string(145,'o')