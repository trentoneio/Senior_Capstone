/****************************************************
This is a script to open the solenoid connected to
digital pin for 30 seconds. In the overall project, 
this is run for 35 seconds, so the 30 second limit
will be enforced.

Author: Trenton Foster
 ****************************************************/
int solPin = 6;

void setup() {
  Serial.begin(9600);
  pinMode(solPin,OUTPUT);
  digitalWrite(solPin, LOW);

}

void loop() {
  digitalWrite(solPin,HIGH);
  delay(30*1000);
  digitalWrite(solPin,LOW);
  delay(30*1000);
}
