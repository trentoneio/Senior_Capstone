# 1 "/home/pi/Desktop/arduino_test/arduino_test.ino"
/* Simple script that flashes an LED */

int PIN = 4;

void setup() {
  Serial.begin(9600);
  pinMode(PIN, 0x1);
  digitalWrite(PIN, 0x0);

}

void loop() {
  digitalWrite(PIN, 0x1);
  delay(500);
  digitalWrite(PIN, 0x0);
  delay(500);

}
