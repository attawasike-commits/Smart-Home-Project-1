// Rain detector project
#include <iostream>

int main() {

const int rainSensorPin = A0; 
const int buzzerPin = 9;
int rainValue = 0; 

void setup() {
  pinMode(rainSensorPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
 
  rainValue = analogRead(rainSensorPin);
  
  Serial.print("Rain Sensor Value: ");
  Serial.println(rainValue);
  
  if (rainValue < 600) {

    digitalWrite(buzzerPin, HIGH);
  } else {
    
    digitalWrite(buzzerPin, LOW);
  }

  delay(500);
}

    return 0;
}