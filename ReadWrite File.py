# To open a file
file = open('test.txt') # Give the exact file path

# Reads all the characters in the file
print(file.read())

# Reads n number of char by passing parameter
print(file.read(5))

# Without parameter reads the 1st line, need to give another time to get the next line
print(file.readline())
print(file.readline())

# Print line by lines using readline method
printLine = file.readline()

while printLine !="":
    print(printLine)
    printLine = file.readline()

# Print line by lines using readlines method
readline = file.readlines() # it will store as list [abc, def, etc.]

for i in readline:
    print(i)

# Always close the file
file.close()