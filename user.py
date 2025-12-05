import json

def writeUser():
    print("Hello, user!")
    data = {}

    data["name"] = input("Enter your name: ", )
    if data["name"]:
        with open("data.json", "w") as file:
            json.dump(data, file, indent = 4)
    else:
        writeUser()
    return data

def getUser():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            return data
    except:
        return writeUser()
    
# FileNotFoundError