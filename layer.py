#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess, time, sys
from sys import exit
import mimetypes
import sys, shutil
from yowsup.layers.interface                           import YowInterfaceLayer,ProtocolEntityCallback     
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity  
from yowsup.layers.protocol_presence.protocolentities  import AvailablePresenceProtocolEntity   
from yowsup.layers.protocol_presence.protocolentities  import UnavailablePresenceProtocolEntity 
from yowsup.layers.protocol_presence.protocolentities  import PresenceProtocolEntity            
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity   
from yowsup.common.tools                               import Jid
from yowsup.layers.protocol_media.mediadownloader      import MediaDownloader
from yowsup.layers.protocol_media.protocolentities     import *
from responses import Response
import random
from config import Cfg

name = "Robozinho"
ALERTAN ="5514981402753@s.whatsapp.net"
class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
		if messageProtocolEntity.getType() == 'text':
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			#Devine mensagem como enviada
			self.toLower(messageProtocolEntity.ack())
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(AvailablePresenceProtocolEntity())
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(PresenceProtocolEntity(name = name))
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			#Devine mensagem como visualisada
			self.toLower(messageProtocolEntity.ack(True))
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_TYPING, Jid.normalize(messageProtocolEntity.getFrom(False))))#Set esta escribiendo
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			#Envia a resposta
			self.onTextMessage(messageProtocolEntity)
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_PAUSED, Jid.normalize(messageProtocolEntity.getFrom(False))))#Set pausa
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			#Fica offline
			self.toLower(UnavailablePresenceProtocolEntity())
		elif messageProtocolEntity.getType() == 'media':
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(AvailablePresenceProtocolEntity())
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(PresenceProtocolEntity(name = name))#Set presencia
			self.onMediaMessage(messageProtocolEntity)
			self.toLower(messageProtocolEntity.ack())
			self.toLower(messageProtocolEntity.ack(True))
			time.sleep(random.randrange(Cfg.RAND_MIN,Cfg.RAND_MAX))
			self.toLower(UnavailablePresenceProtocolEntity())#Set offline

	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		self.toLower(entity.ack())
		
	def onTextMessage(self,messageProtocolEntity):
		name   = messageProtocolEntity.getNotify()
		text    = messageProtocolEntity.getBody()
		sender  = messageProtocolEntity.getFrom()
		textmsg    = TextMessageProtocolEntity
		if messageProtocolEntity.getFrom(False):
			resp = Response()
			answer = resp.getResp(text,name,sender)
			if answer and answer.strip():
				if sender.lower().find("-") == -1:
					self.toLower(textmsg(answer, to = sender ))
					print "\nMensagem pessoal"
					print str(answer)
				else:
					self.toLower(textmsg(answer, to = sender ))
					print "\nMensagem grupo"
					print str(answer)
		else:
			answer = "Oi "+name+", o comando não esta na lista de respostas.\n"
			print sender + "\n"
			print text + "\n"
			if sender.lower().find("-") == -1:
				time.sleep(1)
				self.toLower(textmsg(answer, to = sender))
				print answer
			else:
				print answer

	def onMediaMessage(self, messageProtocolEntity):
		if (messageProtocolEntity.getFrom(False)
		    and messageProtocolEntity.getMediaType() == "image"):
			url = messageProtocolEntity.url
			self.extension = self.getExtension(messageProtocolEntity.getMimeType())
			return self.downloadMedia(url)

	def downloadMedia(self, url):
		print("Download %s" % url)
		downloader = MediaDownloader(self.onSuccess, self.onError, self.onProgress)
		downloader.download(url)

	def onError(self):
		print "Erro ao baixar"

	def onSuccess(self, path):
		outPath = "/home/yowsup/imgs/%s%s" % (os.path.basename(path), self.extension)
		shutil.copyfile(path, outPath)
		print("\nImagen descargada en %s" % outPath)

	def onProgress(self, progress):
		sys.stdout.write("Progreso descarga => %d%% \r" % progress)
		sys.stdout.flush()

	def getExtension(self, mimetype):
		type = mimetypes.guess_extension(mimetype.split(';')[0])
		if type is None:
			raise Exception("Unsupported/unrecognized mimetype: "+mimetype);
		return type