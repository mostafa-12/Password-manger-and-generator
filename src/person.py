class Person:
    def __init__(self, userName, password, dictPassword =None):
        self.userName = userName
        self.password = password
        self.dictPassword= dictPassword if dictPassword is not None else []

    def toDict(self):
        return {
            "Name" : self.userName,
            "Password" : self.password,
            "passwords" : self.dictPassword
        }
    
    def showInfo(self):
        return self.dictPassword  
    @classmethod 
    def creatPerson(cls, user):
        return cls(user["Name"], user["Password"], user["passwords"])