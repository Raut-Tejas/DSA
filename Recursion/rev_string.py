def rev_string(str):
    if len(str)<=1:
        return str
    return rev_string(str[1:]) + str[0]

x="hello"
print(rev_string(x))