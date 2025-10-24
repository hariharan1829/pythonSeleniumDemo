
# List data type -- Allows multiple values and can be different data types

array = [1, 2, 3, "Four", "Five"]

print(array) #output [1, 2, 3, 'Four', 'Five']

print(array[2]) #output 3 (prints the 2nd index in the array)

print(array[-1]) #output Five (prints the last value in the array)

print(array[1:3]) #output [2, 3] (prints from and to of the array)

array.insert(3, "Three") # Insert the new value in that index

print(array) #output [1, 2, 3, 'Three', 'Four', 'Five']

array.append("Six") # Insert the new value at the End [1, 2, 3, 'Three', 'Four', 'Five', 'Six']

print(array) #output [1, 2, 3, 'Three', 'Four', 'Five', 'Six']

array[6] = 6 #Update

print(array) #output [1, 2, 3, 'Three', 'Four', 'Five', 6]

del array[6] # Delete

print(array) #output [1, 2, 3, 'Four', 'Five', 6]

count=len(array) # To count number of char in the list
print(count)