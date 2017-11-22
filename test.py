import serial
from time import sleep

ser = serial.Serial('COM3', baudrate = 9600)
Data = []

def this():
    while True and ser.isOpen():
        sleep(1)
        arduinoData = ser.readline().strip().decode()
        print(arduinoData)
        Data.append(arduinoData)
        print(Data)

#def test(here):
    #return here

#print (test(this()))

print(this())  




'''while True and ser.isOpen():
    arduinoData = ser.readline().strip().decode()
    #print(arduinoData)
    Data.append(arduinoData)'''


