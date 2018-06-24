from stack import YowsupSendStack



admin_number = '553187390685@s.whatsapp.net'

def send_simple_message(message):
    try:
        stack = YowsupSendStack(("5514981402753", "if3VMVGYTaAx0Zgtq1+5Xj+Cun4="), [(admin_number, message)])
        stack.start()
    except:
       pass

send_simple_message('Boa noite!')