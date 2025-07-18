int sensorpin=A0;
int pump=13;
int moisture;
int moisturethreshold=150;
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensorpin, INPUT);
  pinMode(pump, OUTPUT);
  digitalWrite(pump, LOW);
  lcd.init();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  moisture=analogRead(sensorpin);
  Serial.print("Moisture: ");
  Serial.println(moisture); 
  while(moisture<=moisturethreshold){
    digitalWrite(pump,HIGH);
    moisture=analogRead(sensorpin);
    delay(500);
    Serial.print("It's Working! Moisture: ");
    Serial.println(moisture); 
    lcd.setCursor(0,0);
    lcd.print("Dryness Level Is:");
    lcd.setCursor(0,1); 
    lcd.print(moisture);
  }
  digitalWrite(pump,LOW);
  lcd.setCursor(0,0);
  lcd.print("Dryness Level Is:");
  lcd.setCursor(0,1); 
  lcd.print(moisture);
  delay(500);

}
