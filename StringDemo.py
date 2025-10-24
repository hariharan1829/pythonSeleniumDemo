# operation like list in strings
str1 = "Hariharan.com"
str2 = "Hariharan firm"
str3 = "Hariharan"
str4 = " Developer "

# To get a character in a particular string
print(str1[2])  # output is r

# To get substring in a string
print(str1[0:4]) # output is Hari

# To concatenate two strings
print(str1 + ' ' + str2) # output is Hariharan.com Hariharan firm

# Substring check, to check weather a string is present in another string
print(str3 in str1)  # output is True

# Split with a character
print(str1.split(".")) # output is ['Hariharan', 'com']

# To remove end white space in string
print(str4.strip())

# To remove left & right white space in string
print(str4.lstrip())
print(str4.rstrip())

