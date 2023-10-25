/****************************************************
This is a script to "open" the servo connected to
digital pin for 30 seconds. In the overall project, 
this is run for 35 seconds, so the 30 second limit
will be enforced.

Author: Trenton Foster
 ****************************************************/
#include <Servo.h>

Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(6);
  myservo.write(0);

}

void loop() {
  
  myservo.write(180);
  delay(30 * 1000);
  myservo.write(0);
  delay(30 * 1000);
}
