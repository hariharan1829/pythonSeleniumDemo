# for Loops __ for and in are the syntax a letter in between to itrate

obj = [1, 2, 3, 4, 5]

for i in obj:
   print(i)

# multiply -- Range is the inbuild one ie (i, j) --> i to j-1

for j in range(1,10):
   print(j*2)

# sum of five natural numbers

summation = 0
for z in range(1,6):
   summation = summation + z
print(summation) #output is 1 to 5

print("*****Adding index**********")
# Adding index

for y in range(1,10,3):
    print(y)  # output is 1 4 7 jumps 3 numbers

print("*****Skiping index**********")
# Skiping index

for A in range(15):
    print(A) #output is 0 to 14