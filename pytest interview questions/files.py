
#How do you read and write files in python ?

file_path = '../test.txt'  # File path
# with open(file_path, "w") as f:      # To write
#     f.write("Hello im writing in this file1")
#     f.write("Hello im writing in this file2")
#     f.write("Hello im writing in this file3")



with open(file_path, "r") as f: # To read
    read = f.readlines()
    print(read)
    for i in read:
        print(i)