
# question 1

# Difference between tuple and list


#Lists are mutable
        #ie we can able to edit or update

my_list = ["one", "two", "three", "five"]

my_list[0] = 100 # updates the 0th index as 100

print(my_list)  # [100, 'two', 'three', 'five']

my_list.append(5) # Adds value 5 in the last index
print(my_list) # [100, 'two', 'three', 'five', 5]

# Tuple are immutable
         # ie,. we cannot update or add values

my_tuple = ("name", "age", "email")

print(my_tuple[1]) # age

#my_tuple[3] = "address"  #'tuple' object does not support item assignment


# what are pythons buildin datatypes?

x = 10 # Integer
y = 3.5 # float
Z = "Five" # String
A = {"Name" : "Hariharan", "Age": 10 } # Dictionary ie key and value peers
B = True
C = False # Boolean
D = [1,2,3] # List
E = (5,6,7) # Tuple