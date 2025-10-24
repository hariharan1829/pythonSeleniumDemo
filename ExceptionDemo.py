# 1) Fail the test when the condition is not met
# ==============================
Incart = 0

# Using raise → manually throws an exception when condition is not met
if Incart != 2:
    raise Exception("Condition fails")   # 'raise Exception' is the keyword

# Using assert → throws AssertionError if condition is false
assert(Incart == 0)   # Same as above, but no need to manually raise

# ==============================
# 2) try–except–finally example

# Case 1: File does NOT exist → goes to except block
try:
    with open('tests.txt', 'r') as reader:   # File does not exist
        print(reader.read())

except Exception as e:   # Catching the actual Python error
    print(e)             # Prints the error message

# Case 2: File exists → executes normally
try:
    with open('test.txt', 'r') as reader:    # File exists
        print(reader.read())

except:                                      # Generic catch (not recommended, better: Exception as e)
    print("Catch triggered")                 # Custom message

finally:
    print("finally triggered")               # Runs ALWAYS, success or failure
