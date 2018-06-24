import requests
class Ip:
    def __init__(self):
        pass
    def getIp(self):
        return requests.get('http://ident.me/').content
