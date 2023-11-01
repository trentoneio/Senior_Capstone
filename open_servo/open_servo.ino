/****************************************************
This is a script to "open" the servo connected to
digital pin for 30 seconds. In the overall project, 
this is run for 35 seconds, so the 30 second limit
will be enforced.

Author: Trenton Foster
 ****************************************************/
#include <Servo.h>

#define Buzzer_Pin 4
#define LED_PIN 5

Servo myservo;

void notify(int freq){
  for(int i=0;i<3;i++){
  digitalWrite(LED_PIN, HIGH);
  tone(Buzzer_Pin,freq);
  delay(100);
  digitalWrite(LED_PIN, LOW);
  noTone(Buzzer_Pin);
  delay(100);
  }
  
}

void setup() {
  Serial.begin(9600);
  myservo.attach(6);
  myservo.write(0);
  pinMode(Buzzer_Pin, OUTPUT);
  pinMode(LED_PIN,OUTPUT);
}

void loop() {
  myservo.write(100);
  delay(10 * 1000);
  notify(500);
  delay(10 * 1000);
  notify(500);
  delay(5 * 1000);
  notify(750);
  notify(750);
  delay(5 * 1000);
  notify(1000);
  myservo.write(0);
  delay(30 * 1000);
  
  
}
