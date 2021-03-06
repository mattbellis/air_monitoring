/* How to use the DHT-22 sensor with Arduino uno
   Temperature and humidity sensor
*/

//Libraries
#include <DHT.h>;
# include <Adafruit_MPL3115A2.h>
Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

//Constants
#define DHTPIN 5     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
unsigned long time;


//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
  Serial.begin(9600);
  dht.begin();
  baro.begin();
}

void loop()
{
    delay(2000);
    //Read data and store it to variables hum and temp
    hum = dht.readHumidity();
    float bar = baro.getPressure()/1000;
    float tempc = baro.getTemperature();
    float tempf = (tempc * 9/5) +32;
    
    //Print temp and humidity values to serial monitor
    Serial.print("Time: ");
    time = millis();
    Serial.print(time/1000.0);
    Serial.print("   ");
    Serial.print("Humidity: ");
    Serial.print(hum);
    Serial.print(" %, Temp: ");
    Serial.print(tempf);
    Serial.print(" F  ");
    Serial.print(bar);
    Serial.println(" pa");
    delay(1000);
}
