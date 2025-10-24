import json

# code Indentation is important because there is no flower brackets like other languages

greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
else:
    print("Condition do not matches")

# Condition Matches

number = 8

if number < 10:
    print("Less than 10")
else:
    print("Greater than 10")

# Less than 10

data_path = 'Data/test_E2E.json'
with open(data_path) as f:
    test_data = json.load(f)
    print(test_data)
    test_list = test_data["data"]
    print(test_list)