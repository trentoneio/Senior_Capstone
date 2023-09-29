int counter = 0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    message = message + " " + String(counter);
    counter++;
    Serial.println(message);
  }
}
