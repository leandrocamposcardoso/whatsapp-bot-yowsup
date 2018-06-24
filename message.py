# -*- coding: utf-8 -*-
class Message:
    def __init__(self,name):
        self.name = name
    def question(self,question):
        if question == 1:
            return 'Olá %s. Tudo bem?? Espero que sim. Aqui é o Fernando '\
        'Borja, do programa Geração de José.\nGostaria de saber se '\
        'você já está sabendo do nosso último evento deste ano, no '\
        'dia 25/11,com o palestrante Rawlinson Rangel, diretamente de '\
        'Curitiba? Se sim, me mande a palavra\nSIM. Se ainda não, e '\
        'deseja saber mais informações, mande a palavra NÃO.'%self.name

        if question == 2:
            return 'Que bom!! E você já fez sua inscrição gratuita? O '\
        'evento vai ser dia 25/11, começando\nàs 9h, na Fábrica de '\
        'Artes da Lagoinha. Fica na rua Formiga, 450 – Bairro Lagoinha. '\
        'O link pra\ninscrição é esse: https://goo.gl/Z4FMfU . É só '\
        'clicar e se inscrever! Te vejo lá? Sim ou Não?'

        if question == 3:
            return 'Então vamos lá: os seminários Geração de José visam passar '\
        'uma visão bíblica sobrecidadania e política, e quais são as '\
        'formas efetivas para a sua participação na gestão da  '\
        'suacidade. Acreditamos que Igreja de Cristo é chamada a se  '\
        'espalhar para ser sal e luz nomundo, e espaços como esses  '\
        'precisam ser ocupados pelos cristãos, caso contrário,  '\
        'serãoocupados por outros que não partilham da fé e dos  '\
        'princípios do Reino de Deus.No nosso último encontro deste ano  '\
        'receberemos o Pr. Rawlinson Rangel. Ele é Graduado  '\
        'emAdministração Pública, Teólogo, Diretor da Vida &  '\
        'Sociedade, organização que oferece oCurso Pólis –  '\
        'Capacitação Política na Cosmovisão Bíblica, Coaching de  '\
        'Vida e ConsultoriaPolítica.'

        if question == 4:
            return 'O link para inscrição gratuita é: https://goo.gl/Z4FMfUE aí, '\
            'nos vemos lá? Sim ou Não?'

        if question == 5:
            return 'Que bom. Estamos preparando um evento excelente pra você. Todas '\
        'as informaçõesnecessárias estão no site '\
        'www.geracaodejose.com.br . Deus te abençoe. Um grande abraço.'

        if question == 6:
            return 'Que pena. Quem sabe no próximo então. Se quiser acompanhar'\
        'nossos outros eventose ficar por dentro do Geração de José, '\
        'é só acessar www.geracaodejose.com.br. Deus teabençoe. Um '\
        'grande abraço.'
        
        if question == 7:
            return 'Não compreendi a sua resposta, poderia repetir?'

