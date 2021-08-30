s1 = "Mike's book"
s2 = 'Mike\'s book' # using escape character to avoid syntax error
print(s1, s2)

# s1[0] = 'a' # strings are immutable 

# copying a string
Str = "string to copy"
newStr = Str 
newStr1 = Str[:]
newStr2 = "".join(Str)
print(newStr)

# reverse a string
revStr = Str[::-1]

opStr = "Basic"
# length of a string
len(opStr)

# concatenate string
print(opStr + " operation")

# repeat string
print(opStr * 3)

# char -> ascii/utf-8
print(ord('a'))
# ascii/utf-8 -> char
print(chr(97))

# memership operation: in
print('p' in "python")