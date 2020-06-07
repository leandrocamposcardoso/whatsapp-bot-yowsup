#!/usr/bin/python
# -*- coding: utf-8 -*-
from yowsup.stacks                             import YowStackBuilder
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from layer                                     import EchoLayer
from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.env                                import YowsupEnv
from layer									   import EchoLayer
import threading, os, subprocess, time, sys

CREDENTIALS = ("5514981402753", "if3VMVGYTaAx0Zgtq1+5Xj+Cun4=")
laye = EchoLayer()

def workerwhatsapp():
	stackBuilder = YowStackBuilder()
	stack = stackBuilder.pushDefaultLayers(True).push(laye).build()
	stack.setCredentials(CREDENTIALS)
	stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
	stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
	stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
	stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())
	stack.loop( timeout = 0.5, discrete = 0.5 )

if __name__==  "__main__":
	threads = []
	wasa = threading.Thread(target=workerwhatsapp)
	threads.append(wasa)
	wasa.start()