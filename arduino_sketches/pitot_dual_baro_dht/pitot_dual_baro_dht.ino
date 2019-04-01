#include "DHT.h"

#define DHTPIN 2 
#define DHTTYPE DHT21  
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>
Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();
float Output = 0;


float offset = 2.5;
const float slope = 1.0;
int count = 0;
int pitot1 = 0;
int pitot2 = 0;
float voltage1 = 0;
float voltage2 = 0;
float Vtot1 = 0;
float Vtot2 = 0;
float offset1 = 0;
float offset2 = 0;
int i = 0;
DHT dht(DHTPIN, DHTTYPE);


void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   dht.begin();

    int nloops = 100;
    float Vtot = 0;
    for (i=0;i<nloops;i++) {
    pitot1 = analogRead(A0);
    pitot2 = analogRead(A1);
    voltage1 = (float) (pitot1 / 1023.0) * 5.0;
    voltage2 = (float) (pitot2 / 1023.0) * 5.0;
      Vtot1 += voltage1;
      Vtot2 += voltage2;
    }
    offset1 = Vtot1/nloops;
    Serial.print(offset1);
    offset2 = Vtot2/nloops;
    Serial.print("\t");
    Serial.print(offset2);

}

void loop() {
  if (! baro.begin()) {
    Serial.println("Couldnt find sensor");
    return;
  }

   
    float h = dht.readHumidity();
    pitot1 = analogRead(A0);
    pitot2 = analogRead(A1);
    voltage1 = (float) (pitot1 / 1023.0) * 5.0;
    voltage2 = (float) (pitot2 / 1023.0) * 5.0;
    float pressure1 = ((voltage1 - offset1) / slope) * 1000;
    float velocity1 = ((2* (pressure1) ) / 1.225);
    float speeed1 = (velocity1 * 2.2);
    float pressure2 = ((voltage2 - offset2) / slope) * 1000;
    float velocity2 = ((2* (pressure2) ) / 1.225);
    float speeed2 = (velocity2 * 2.2);
    float barr = baro.getPressure();
    float bar = (barr / 1000);
    float tempc = baro.getTemperature();
    float tempF = (tempc * 9/5) + 32;
    char buffer[256];
    //int i = sprintf(buffer, "%f", voltage1);
    //int f = sprintf(buffer, "%f", voltage2);

    float vel1 = 0;
    if (velocity1 > 0.0) { vel1 = sqrt(velocity1);
    }
    float vel2 = 0;
    if (velocity2 > 0.0) { vel2 = sqrt(velocity2);
    }    
    Serial.print(millis()/1000.0,4);
    Serial.print(" ");
    Serial.print(offset1);
    Serial.print(" ");
    Serial.print(pitot1);
    Serial.print(" ");
    Serial.print(voltage1);
    Serial.print(" ");
    Serial.print(vel1);
    Serial.print (" ");
    Serial.print(pressure1);
    Serial.print("   ");
    Serial.print(" ");
    Serial.print(offset2);
    Serial.print(" ");
    Serial.print(pitot2);
    Serial.print(" ");
    Serial.print(voltage2);
    Serial.print(" ");
    Serial.print(vel2);
    Serial.print(" ");
    Serial.print(pressure2);
    Serial.print("    ");
    Serial.print(bar);
    Serial.print(" ");
    Serial.print(tempF);
    Serial.print(" ");
    Serial.print(h);
    Serial.print("\n");
    delay(1000);

}
