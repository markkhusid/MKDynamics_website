
/*
  Analog Input
 Demonstrates analog input by reading an analog sensor on analog pin 0 and
 turning on and off a light emitting diode(LED)  connected to digital pin 13. 
 The amount of time the LED will be on and off depends on
 the value obtained by analogRead(). 
 
 The circuit:
 * Potentiometer attached to analog input 0
 * center pin of the potentiometer to the analog pin
 * one side pin (either one) to ground
 * the other side pin to +5V
 * LED anode (long leg) attached to digital output 13
 * LED cathode (short leg) attached to ground
 
 * Note: because most Arduinos have a built-in LED attached 
 to pin 13 on the board, the LED is optional.
 
 
 Created by David Cuartielles
 modified 30 Aug 2011
 By Tom Igoe
 
 modified by Mark Khusid 12 Jan 2015
 
 This example code is in the public domain.
 
 http://arduino.cc/en/Tutorial/AnalogInput
 
 */

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin2 = 2;      // select the pin for the LED
int ledPin3 = 3;
int ledPin4 = 4;
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin2, OUTPUT);  
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("Hello world!");
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);    
  Serial.println(sensorValue);
  if (sensorValue <= 341) 
  // turn the ledPin on
    digitalWrite(ledPin2, HIGH);
  else if ((sensorValue > 341) && (sensorValue <= 682))
    digitalWrite(ledPin3, HIGH);  
  else if ((sensorValue > 683) && (sensorValue <= 1023))
    digitalWrite(ledPin4, HIGH);
  // stop the program for <sensorValue> milliseconds:
  delay(sensorValue);          
  // turn the ledPin off:        

  if (sensorValue <= 341) 
  // turn the ledPin on
    digitalWrite(ledPin2, LOW);
  else if ((sensorValue > 341) && (sensorValue <= 682))
    digitalWrite(ledPin3, LOW);  
  else if ((sensorValue > 683) && (sensorValue <= 1023))
    digitalWrite(ledPin4, LOW);

  // digitalWrite(ledPin2, LOW);   
  // digitalWrite(ledPin3, LOW);   
  // digitalWrite(ledPin4, LOW);   
  // stop the program for for <sensorValue> milliseconds:
  delay(sensorValue);                  
}
