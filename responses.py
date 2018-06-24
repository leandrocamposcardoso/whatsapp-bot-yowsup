# -*- coding: utf-8 -*-
from modules.mdl_ip import Ip
from config import Cfg
from states import States
from database import Database
from user import User
from message import Message
import datetime
import time

# emojis = {
#     'robot':u'🤖'
# }
states = {}
class Response:
    def __init__(self):
        self.greetings = ['oi','ola','olá']
        self.ok = ['sim','s']
        self.nope = ['não','nao','n']
        self.gabinete = ['1','gabinete']
        self.projetos = ['2','projetos']

    def getResp(self,text,name,sender):
        global states
        response = ''
        #timestamp
        ts = time.time()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #phone
        phone =  sender.split('@')[0][2:]
        #Create states
        if not name in states:
            states[name]=States.MainMenu
       

        #Connect to DB
        db = Database()
        
        # try:
        #     query = """SELECT * FROM users WHERE phone = %s """%phone
        #     user = db.query(query)
        #     usr = User(user[0]['name'],user[0]['phone'],user[0]['notify'],user[0]['creation'])
        # except:
        #     query = """INSERT INTO `users` (`name`,`phone`,`notify`,`creation`) VALUES ('%s','%s','%s','%s')"""%(name.decode('utf8'),phone,'0',timestamp)
        #     query2 = """INSERT INTO `questionary` (`user_phone`,`q_1`,`q_2`,`creation`) VALUES ('%s','%s','%s','%s')"""%(phone,'0','0',timestamp)
        #     db.insert(query)
        #     db.insert(query2)  
        #     usr = User(name,phone,'0',timestamp)
            

        firstname = name.split(" ")[0]
        #Messages
        ms = Message(firstname)
        text = text.encode('utf8')
        msg =  'State:'+str(states[name])+'\n'+name+': '+text+''
        print msg
        #Inicio
        if text.lower() in self.greetings:
            #Estado MainMenu
            states[name]=States.MainMenu
            response = ms.question(1)

        elif states[name]==States.MainMenu and text.lower() in self.ok:
            #Estado Inscricao
            states[name]=States.Inscricao
            response = ms.question(2)

        elif states[name]==States.MainMenu and text.lower() in self.nope:
            #Aprovou Inscricao
            states[name]=States.Inscricao
            response = ms.question(3)
        
        elif states[name]==States.Inscricao:
            #Não aprovou Gabinete
            states[name]=States.Confirm
            response = ms.question(4)
        
        elif states[name]==States.Confirm and text.lower() in self.ok:
            #Envia notificação
            #Estado MainMenn
            states[name]=''
            response = ms.question(5)

        elif states[name]==States.Approved and text.lower() in self.nope:
            #Não envia notificação
            states[name]=''
            response = ms.question(6)
        else:
            response = ms.question(7)
        return str(response)