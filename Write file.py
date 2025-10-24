# Previously we use open and close to open a file, now we going to use in optimized way

# The Goal is to reverse the content in the file

with open('test.txt','r') as reader:         # optimized way to open and close; r means reader mode
    content = reader.readlines()
    reversed(content)                        # to reverse the content
    with open('test.txt','w') as writer:
        for i in reversed(content):          # loop for writing in file
            writer.write(i)                  # Write command

with open('test.txt','r') as reader1:
    print(reader1.readlines())