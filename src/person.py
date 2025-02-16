class Person:
    def __init__(self, userName, password, mail, passwordList):
        self.userName = userName
        self.password = password
        self.mail = mail
        self.passwordList = passwordList

    def toDict(self):
        return {
            "Name" : self.userName,
            "Password" : self.password,
            "Mail" : self.mail,
            "passwords list" : self.passwordList
        }