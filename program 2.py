def reverse_string(str):
    words=str.split()
    reversed_string=''.join(reversed(words))
    return reversed_string
str="We are the future"
result=reverse_string(str)
print(result)

