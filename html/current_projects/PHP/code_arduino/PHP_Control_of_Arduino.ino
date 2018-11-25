
/*
 http://www.instructables.com/id/Control-an-Arduino-with-PHP/step4/How-it-works-the-Arduino-side/
 
 modified by Mark Khusid 12 Jan 2015
 
 This example code is in the public domain.
 
 
 */

int ledPin2 = 2;      // select the pin for the LED
int ledPin3 = 3;
int ledPin4 = 4;
int usbnumber = 0; //this variable holds what we are currently reading from serial
int const led_delay=250;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin2, OUTPUT);  
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  
  Serial.begin(9600);
  // Serial.println("Hello world!");
}

void loop() {
  
//  Serial.println("Heartbeat \n");
  
  if (Serial.available() > 0) { //if there is anything on the serial port, read it
        usbnumber = Serial.read(); //store it in the usbnumber variable
        Serial.print("Incoming Data -> ");
        Serial.println(usbnumber);  
  }
  
  if (usbnumber == 49) { 
    digitalWrite(ledPin2, HIGH);
    Serial.println("USB Number is 1");
    Serial.println("Heartbeat");
    delay(led_delay);
    digitalWrite(ledPin2, LOW);
  }  
  else if (usbnumber == 50) {    
    digitalWrite(ledPin3, HIGH);  
    Serial.println("USB Number is 2");
    Serial.println("Heartbeat");
    delay(led_delay);
    digitalWrite(ledPin3, LOW);
  }  
  else if (usbnumber == 51) {    
    digitalWrite(ledPin4, HIGH);
    Serial.println("USB Number is 3");
    Serial.println("Heartbeat");
    delay(led_delay);
    digitalWrite(ledPin4, LOW);
  }
  // stop the program for 1000 milliseconds:
  delay(led_delay);          

//  // turn the ledPin off:        
//
//  if (sensorValue <= 341) 
//  // turn the ledPin on
//    digitalWrite(ledPin2, LOW);
//  else if ((sensorValue > 341) && (sensorValue <= 682))
//    digitalWrite(ledPin3, LOW);  
//  else if ((sensorValue > 683) && (sensorValue <= 1023))
//    digitalWrite(ledPin4, LOW);
//
  // digitalWrite(ledPin2, LOW);   
  // digitalWrite(ledPin3, LOW);   
  // digitalWrite(ledPin4, LOW);   
  // stop the program for for <sensorValue> milliseconds:
//  delay(1000);                  
}
