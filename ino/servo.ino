#include <Servo.h>

Servo myservo;  
Servo myservo2;

byte incomingByte[2];
void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  myservo2.attach(10);
}
void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(incomingByte,2);
    myservo.write(incomingByte[0]);    
    myservo2.write(incomingByte[1]);
  }
}
