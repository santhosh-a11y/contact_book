import json

operation = (input("enter operation: "))

# a function to get inputs from the user
def enterr():
    try:
        with open("contacts.txt", "r") as i:
            contacts_dict = json.load(i)
    
    except FileNotFoundError:
        contacts_dict = {}

    while True:
        a = input("name: ")
        if a == "x":
            break
        b = int(input("contacts: "))

        contacts_dict[a] = b
    
    with open("contacts.txt", "w") as i:
        json.dump(contacts_dict, i)


# a function to view the stored values
def seee():
    with open("contacts.txt", "r") as i:
        content = json.load(i)
        print(content)


# calling the enter function
if operation == "write":
    enterr()
# calling the see function
elif operation == "see":
    seee()
