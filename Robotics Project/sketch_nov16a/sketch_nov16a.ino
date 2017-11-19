
int soil = A0;
int LED = 9;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(soil, INPUT);
  pinMode(LED, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int readVal = analogRead(soil);
  Serial.println(readVal);
  if(readVal >= 600)
  {
    digitalWrite(LED,HIGH);  
  }
  else if(readVal <= 500) 
  {
    digitalWrite(LED, LOW);
  }else
  {
    digitalWrite(LED, HIGH);  
    delay(500);
    digitalWrite(LED, LOW);
  }

}
