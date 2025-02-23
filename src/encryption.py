from cryptography.fernet import Fernet
import bcrypt
import os
import json
import person


path = os.path.dirname(os.path.dirname(__file__)) + r"\data\key.key" # get key path
Key=bytes() 
Cipher = None 


def creatKeyIfNot():  #creat key if not exists and initialize value to cipher
    global Key,Cipher
    if os.path.isfile(path=path):
        with open(path,"rb") as file:
            Key=file.read()
            
    else:
        with open(path,"wb") as file:
            
            Key = Fernet.generate_key()
            file.write(Key)
            
    Cipher = Fernet(Key)        


def Encrypt(Person):
    global Cipher
    data = Person.toDict()
    passwordsJson = json.dumps(data["passwords"]).encode()
    data["passwords"] = Cipher.encrypt(passwordsJson).decode()
    return person.Person.creatPerson(data)
def Decrypt(person):
    global Cipher
    
    data = person.toDict()
    
    passwordsJson = json.loads(data["passwords"]).encode()
    
    data["passwords"] = Cipher.decrypt(passwordsJson)

def hashing(Person):
    userInfo = Person.toDict()
    userName = userInfo["Name"].encode()
    userPassword = userInfo ["Password"].encode()
    userSlat = bcrypt.gensalt()
    passwordSlat = bcrypt.gensalt()
    userInfo["Name"] = bcrypt.hashpw(userName,userSlat).decode()
    userInfo["Password"] = bcrypt.hashpw(userPassword,passwordSlat).decode()
    return person.Person.creatPerson(userInfo)
def atLogin(name, password, person):
    userInfo = person.toDict()
    if bcrypt.checkpw(name.encode(),userInfo["Name"]) and bcrypt.checkpw(password.encode(),userInfo["Password"]):
        return True
    else:
        return False



