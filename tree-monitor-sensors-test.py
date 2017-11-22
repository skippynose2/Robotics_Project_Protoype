import json
from random import *
from time import sleep

dataFile = open('data.json', 'r')
data = json.loads(dataFile.read())
dataFile.close()

while True:
	arduinoData = randint(1, 1000)
	data.append(arduinoData)
	data = data[-50:]
	print(data)
	dataFile = open('data.json', 'w')
	json.dump(data, dataFile)
	dataFile.close()
	sleep(1)
