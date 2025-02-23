import secrets
import string
import person
import json
import os
import bcrypt

dataPath = os.path.dirname(os.path.dirname(__file__)) + r"\data"

dataFile =dataPath + r"\users.json"
def generatePassword(length = 8):
    src = string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    password = ""
    for l in range(length):
        password +=secrets.choice(src)
    return password

def generateToken():
    return secrets.token_hex()

def creatAccount(userName,password):
    
    return person.Person(userName,password)

def addPass(person, password):
    
    data = person.toDict()
    if password not in data["passwords"]:
        data["passwords"].append(password)
    else:
        print(f"{password} is already exist")

def removePass(person, password):
    data = person.toDict()
    if password in data["passwords"]:
        del data["passwords"][data["passwords"].index(password)]
    else:
        print(f"{password} is not already exist")

def saveUser(person):
    user = person.toDict()
    if os.path.isfile(dataFile) == False :
        with open(dataFile,"w") as file :
             initFile = {"users" :[]}
             json.dump(initFile, file)
    with open(dataFile,"r") as file :
        users = json.load(file)
    with open(dataFile,"w") as file :
        users["users"].append(user)
        json.dump(users, file, indent = 2)

            
def loadUser(userName,password):
    userName = userName.encode()
    password = password.encode()
    with open(dataPath,"r") as file:
        users = json.load(file)
        
    for user in users["users"]:
        if bcrypt.checkpw(userName, user["Name"]) and bcrypt.checkpw(password, user["Password"]):
            print("hello ",userName.decode())
            return person.createPerson(user)
        else:
            print("user name or password is wrong please check your data and try again later")
            return False
    