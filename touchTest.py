#!/usr/bin/env python
import inspect
import colorsys
import sys
import time

import flotilla

from phue import Bridge

def initializeFlotillaTouch():

	try:
	    dock = flotilla.Client(
	       requires={
		    'one': flotilla.Touch
		})
	except KeyboardInterrupt:
	    sys.exit(1)

	while not dock.ready:
	    pass

	touch = dock.first(flotilla.Touch)
	return dock, touch

def getLightInfo(lightIndex):
	lights = b.get_light_objects('id')
	light = lights[lightIndex]
	members = vars(light)
	print members

def performNextAction(lightIndex):
	nextAction = actions[lightAction[lightIndex - 1]]
	
	lights = b.get_light_objects('id')
	light = lights[lightIndex]
	
	print 'setting ' + nextAction['key'] + ':' + str(nextAction['value'])
	setattr(light, nextAction['key'], nextAction['value'])
	
	lightAction[lightIndex - 1] = lightAction[lightIndex - 1] + 1
	
	if lightAction[lightIndex - 1] >= len(actions):
		lightAction[lightIndex - 1] = 0

def flotillaTouchListen(touch):
	try:
	    while True:

		if touch.one:
			performNextAction(1)
		if touch.two:
			performNextAction(2)
		if touch.three:
			performNextAction(3)
		if touch.four:
			performNextAction(4)	
		
		time.sleep(0.1)

	except KeyboardInterrupt:
	    print("Stopping Flotilla...")




b = Bridge('192.168.0.50')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
b.get_api()

dock, touch = initializeFlotillaTouch()

actions = [{'key': 'on', 'value': True}, {'key': 'colortemp', 'value': 123}, {'key': 'colortemp', 'value': 567}, {'key': 'on', 'value': False}]
lightAction = [0, 0]

flotillaTouchListen(touch)

dock.stop()
