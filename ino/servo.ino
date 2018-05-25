/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
Servo myservo2;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
byte incomingByte[2];
void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  myservo2.attach(10);// attaches the servo on pin 9 to the servo object
}

void loop() {
  if (Serial.available() > 0) {
  
    // read the incoming byte:
    Serial.readBytes(incomingByte,2);
    myservo.write(incomingByte[0]);    
    myservo2.write(incomingByte[1]);
  }
  
//  
//  for (pos = 0; pos <= 140; pos += 5) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    myservo.write(pos);    
//    myservo2.write(pos);// tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
//  for (pos = 140; pos >= 0; pos -= 5) { // goes from 180 degrees to 0 degrees
//    myservo.write(pos);
//    myservo2.write(pos);// tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
}