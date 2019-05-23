#include "DHT.h"

#define DHTPIN 2 
#define DHTTYPE DHT21 // THis should be good for the DHT 2301 sensor  
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>
Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();




float V_0 = 5.0; // supply voltage to the pressure sensor
float rho = 1.204; // air density

// parameters for averaging and offset
float veloc = 0.0;
float veloc2 = 0.0;
float offset = 0.0;
float offset2 = 0.0;
float offset_size = 100;
float veloc_mean_size = 20l;
float zero_span = 2;
float voltage = 0.0;
float voltage2 = 0.0;
float V1 = 0.0;
float V2 = 0.0;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // setup and calculate offset
  Serial.begin(9600);
  for (int ii=0;ii<offset_size;ii++){
    offset += analogRead(A0)-(1023/2);
    offset2 += analogRead(A1)-(1023/2);
  }
  offset /= offset_size;
  offset2 /= offset_size;
}

void loop() {
  float adc_avg = 0; float veloc = 0.0; float adc_avg2 = 0; float veloc2 = 0.0;

  //average a few ADC readings for stability 
  for (int ii=0;ii<veloc_mean_size;ii++){
    adc_avg+= analogRead(A0)-offset;
    adc_avg2+= analogRead(A1)-offset2;
  }
  adc_avg/=veloc_mean_size;
  adc_avg2/=veloc_mean_size;

  voltage = (adc_avg/1023)*5;
  voltage2 = (adc_avg/1023)*5;


  // make sure if the ADC reads below 512 then its a negative velocity
  if (adc_avg>512-zero_span and adc_avg<512+zero_span){
  } else{
    if (adc_avg<512){
      veloc = -sqrt((-10000.0*((adc_avg/1023.0)-0.5))/rho);
    } else {
      veloc = sqrt((10000.0*((adc_avg/1023.0)-0.5))/rho);
    }
  }

if (! baro.begin()) {
    Serial.println("Couldnt find sensor");
    return;
  }
  float h = dht.readHumidity(); float dht_f = dht.readTemperature(true);
  float barr = baro.getPressure();
  float bar = (barr / 1000);
  float tempc = baro.getTemperature();
  float tempF = (tempc * 9/5) + 32;


  // same as before but for the second pitot tube
  if (adc_avg2>512-zero_span and adc_avg2<512+zero_span){
  } else{
    if (adc_avg2<512){
      veloc2 = -sqrt((-10000.0*((adc_avg2/1023.0)-0.5))/rho);
    } else {
      veloc2 = sqrt((10000.0*((adc_avg2/1023.0)-0.5))/rho);
    }
  }
  
   // Volume Calculation
   V1 = PI * (0.0254)*(0.0254) * veloc;
   V2 = PI * (0.0254)*(0.0254) * veloc2;

  
  Serial.print(veloc); 
  Serial.print(" m/s ");
  Serial.print(V1,4);
  Serial.print(" m^3/s ");
  Serial.print(adc_avg);
  Serial.print(" bits ");
  Serial.print(voltage);
  Serial.print(" Volts   ");
  Serial.print(veloc2);
  Serial.print(" m/s ");
  Serial.print(V2,4);
  Serial.print(" m^3/s ");
  Serial.print(adc_avg2);
  Serial.print(" bits ");
  Serial.print(voltage2);
  Serial.print(" Volts   ");
  Serial.print(bar);
  Serial.print(" kPa ");
  Serial.print(h);
  Serial.print(" ");
  Serial.print(tempF);
  Serial.println("F ");
  delay(100);
}
