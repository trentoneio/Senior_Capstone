#include <Arduino.h>
#line 1 "/home/pi/Desktop/arduino_test/arduino_test.ino"
/* Simple script that flashes an LED */

int PIN = 4;

#line 5 "/home/pi/Desktop/arduino_test/arduino_test.ino"
void setup();
#line 12 "/home/pi/Desktop/arduino_test/arduino_test.ino"
void loop();
#line 5 "/home/pi/Desktop/arduino_test/arduino_test.ino"
void setup() {
  Serial.begin(9600);
  pinMode(PIN, OUTPUT);
  digitalWrite(PIN, LOW);

}

void loop() {
  digitalWrite(PIN, HIGH);
  delay(500);
  digitalWrite(PIN, LOW);
  delay(500);

}

