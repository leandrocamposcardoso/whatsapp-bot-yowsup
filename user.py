class User:
    def __init__(self,name,phone,notify,date):
        self.name = name
        self.phone = phone
        self.notify = notify
        self.date = date
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getNotify(self):
        return self.notify
    def getDate(self):
        return self.date
  