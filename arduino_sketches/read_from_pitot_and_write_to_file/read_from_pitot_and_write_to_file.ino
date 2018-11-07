// Started from here
// https://forum.arduino.cc/index.php?topic=226279.0


// The offset voltage is 1.0V when there is no pressure difference.
const float offset = 2.7077;

// The sensitivity is 1.0V per kPa for the sensor.
const float sensitivity = 1.0;


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int rawADC = analogRead(A0);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = rawADC * (5.0 / 1023.0);
  
  // print out the value you read:
  float pressure = (voltage - offset) / sensitivity;   // differential pressure in kPa
  pressure *= 1000.0; // Convert to Pa
  
  // Some magical calcuation for the windspeed (just as an example)
  float air_density = 1.29; // kg/m^3
  float windspeedsq = ( 2.0 * pressure / air_density );
  
  float windspeed = 0.0;
  if (windspeedsq > 0.0) {
    windspeed = sqrt(windspeedsq);
  }
  
  Serial.print(millis()/1000.0,4);
  Serial.print(" ");
  Serial.print(rawADC,DEC);
  Serial.print(" ");
  Serial.print(sensitivity,4);
  Serial.print(" ");
  Serial.print(offset,4);
  Serial.print(" ");
  Serial.print(voltage,4);
  Serial.print(" ");
  Serial.print(pressure,4);
  Serial.print(" ");
  Serial.print(windspeed,4);
  Serial.print("\n");
  
  delay(1000); // ms
  
}
