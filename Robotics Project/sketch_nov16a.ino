#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0X27,16,2);
int sensor = A0;
Servo myServo;
int servoPin = 9;

void setup() {
  // put your setup code here, to run once:
  lcd.begin();
  Serial.begin(9600);
  myServo.attach(servoPin);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(5000);
  int servo;
  int readVal = analogRead(sensor);
  Serial.println(readVal);
  lcd.clear();
  lcd.print(readVal);
  if (readVal >= 600)
  {
    myServo.write(180);
  }else if (readVal <= 500) 
  {
    myServo.write(0);  
  }

}
