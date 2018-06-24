# -*- coding: utf-8 -*-
from modules.mdl_ip import Ip
from config import Cfg
from states import State
from database import Database
from user import User
from states import States
import datetime
import time

emojis = {
    'robot':u'🤖'
}
states = {}
greetings = ['oi','ola','olá']
ok = ['sim','s']
nope = ['não','nao','n']
class Response:
    def __init__(self):
        pass

    def getResp(self,text,name,sender):
        
        #timestamp
        ts = time.time()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        telefone =  sender.split('@')[0][2:]
        #DB check
        try:
            db = Database()
            query = """SELECT * FROM users WHERE phone = %s """%telefone
            user = db.query(query)
            usr = User(user[0]['name'],user[0]['phone'],user[0]['notify'],user[0]['creation'])
        except:
            query = """INSERT INTO `users` (`name`,`phone`,`notify`,`creation`) VALUES ('%s','%s','%s','%s')"""%(name,telefone,'0',timestamp)
            db.insert(query) 
            usr = User(name,telefone,'0',timestamp)

        if not name in states:
            states[name]=''
        response = ''
        
        name = name.split(" ")[0]
        text = text.encode('utf8')
        msg =  name+': '+text+''
        print msg
        #Inicio menu
        if text.lower() in greetings:
            #Estado MainMenu
            states[name]=States.MainMenu
            response = ''




        #Introducao
        if text.lower() in greetings:
            states[name]='menu1'
            response = 'Olá prezado %s, tudo bem? Aqui é o Fernando Borja, '\
            'vereador, e gostaria de agradescer demais a sua vinda aqui no '\
            'Gabinete, viu? Queria saber se você aprovou o atendimento que '\
            'recebeu aqui? Se puder digitar SIM, em caso positivo; ou NÂO, '\
            'em caso, negativo. Isso nos ajudará a entender melhor o nosso '\
            'eleitorado'%name
        #sim
        elif text.lower() in ok and 'menu1' in states.values():
            states[name]='menu2'
            response = 'Puxa, muito obrigado %s. Ficamos felizes com seu feedback '\
            'positivo. Aproveitando o ensejo, você gostaria de receber noticias do '\
            'Gabinete por aqui? Se puder digitar SIM, em caso positivo; ou NÃO, em '\
            'caso negativo. Mais uma vez agradecemos o seu retorno. Abração'%name

        elif text.lower() in nope and 'menu1' in states.values():
            states[name]='feedback'
            response = 'Puxa %s, peço de coração que nos perdoe pela experiência negativa '\
            'Gostaria de entender melhor a sua insatisfação. Coloquei como prioridade aqui '\
            'no gabinete o atendimento exemplar aos cidadãos. Você poderia me dar um feedback '\
            'do que não gostou?'%name
        
        #Menu 2
        #sim
        elif text.lower() in ok and 'menu2' in states.values():
            states[name]=''
            response = 'Obrigado pelo retorno. Enviaremos, então, notícias do mandato '\
            'para você. Grande abraço e que Deus te abençoe. Fernando Borja.'
            #Atualiza banco
            query = """UPDATE users SET notify='1' WHERE phone=%s """%usr.getPhone()
            db.insert(query)
        #não
        elif text.lower() in nope and 'menu2' in states.values():
            states[name]=''
            response = 'Claro, fique tranquilo. entendemos que as vezes o whatsapp fica '\
            'cheio demais, e não queremos ser  \"spam\" para você. Continuaremos contando '\
            'com você, com seus feedbacks e com suas orações. Que Deus te abençoe.\nFernando Borja'  
       
        elif 'feedback' in states.values():
            states[name]=''
            query = """INSERT INTO `feedback` (`user_phone`,`feedback`,`creation`) VALUES ('%s','%s','%s')"""%(telefone,text,timestamp)
            db.insert(query) 
            response = 'Mais uma vez pedimos mil perdões por qualquer inconveniente. Levarei essa '\
            'mensagem a todo o gabinete, e daremos um retorno em breve a você. Abraços e que Deus te '\
            'abençoe. Fernando Borja.'
            
        else:
            response = name+' nao entendi o que você disse. Poderia repetir?'
        
        return str(response)