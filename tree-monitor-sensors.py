import serial
import json
from time import sleep

ser = serial.Serial('COM3', baudrate = 9600)
dataFile = open('data.json', 'r')
data = json.loads(dataFile.read())
dataFile.close()

while True and ser.isOpen():
	arduinoData = ser.readline().strip().decode()
	data.append(arduinoData)
	data = data[-50:]
	print(data)
	dataFile = open('data.json', 'w')
	json.dump(data, dataFile)
	dataFile.close()
	sleep(1)
