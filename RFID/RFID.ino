//Viral Science

/****************************************************
The following features edits to fit the Smart_Mailbox
project.

Edits made by Trenton Foster
 ****************************************************/


//RFID
#include <MFRC522.h>
#include <Servo.h>
 
#define SS_PIN 10
#define RST_PIN 9
int LED_PIN = 5;
int Buzzer_Pin = 4;
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance

void notify(){
  digitalWrite(LED_PIN, HIGH);
  tone(Buzzer_Pin,500);
  delay(100);
  digitalWrite(LED_PIN, LOW);
  noTone(Buzzer_Pin);
  delay(100);
}
 
void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();
  mfrc522.PCD_Init();   // Initiate MFRC522
  pinMode(LED_PIN, OUTPUT);
  pinMode(Buzzer_Pin, OUTPUT);
  Serial.println("Put your card to the reader...");
  Serial.println();
  tone(Buzzer_Pin, 500);
  delay(2000);
  noTone(Buzzer_Pin);
  

}
void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();
  // Notify user of RFID read
  notify();
  if (content.substring(1) == "B8 B1 8C 12") //change here the UID of the card/cards that you want to give access
  {
    // Notify user of user RFID read (notify() ran 2 times total)
    notify();
    Serial.println("User access");
    Serial.println();
    // Delay to save RPi resources
    delay(1000);
  }

   else if (content.substring(1) == "72 05 95 51")
   {
    Serial.println("Master access");
    Serial.println();
    // Delay to save RPi resources
    delay(1000);
   }
 else   {
    Serial.println(" Access denied");
    // Notify user of incorrect RFID read (notify() ran 3 times total)
    notify();
    notify();
  }
} 
