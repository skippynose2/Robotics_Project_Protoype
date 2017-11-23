import serial
import json
from time import sleep
from datetime import datetime

ser = serial.Serial('COM3', baudrate = 9600)
dataFile = open('data.json', 'r')
data = json.loads(dataFile.read())
dataFile.close()

while True and ser.isOpen():
	arduinoData = int(ser.readline().strip().decode())
	date = str(datetime.now())
	data.append([arduinoData,date])
	data = data[-50:]
	print(data)
	dataFile = open('data.json', 'w')
	json.dump(data, dataFile)
	dataFile.close()
	sleep(3600)
