import serial
from time import sleep

ser = serial.Serial('COM3', baudrate = 9600)
file = open(“data.json”, “w”)
data = file.read()

while True and ser.isOpen():
	arduinoData = ser.readline().strip().decode()
	data.append(arduinoData)
	data = data[-50:]
	json.dump(data, file)
	sleep(1)
