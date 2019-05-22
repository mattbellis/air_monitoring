float V_0 = 5.0; // supply voltage to the pressure sensor
float rho = 1.204; // air density

// parameters for averaging and offset
int veloc = 0;
int veloc2 = 0;
int offset = 0;
int offset2 = 0;
int offset_size = 100;
int veloc_mean_size = 20l;
int zero_span = 2;
int pressure1 = 0;
int pressure2 = 0;

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

  // Calculate pressure
  pressure1 = (adc_avg - offset)*1000;
  pressure2 = (adc_avg2 - offset2)*1000;

  // make sure if the ADC reads below 512 then its a negative velocity
  if (adc_avg>512-zero_span and adc_avg<512+zero_span){
  } else{
    if (adc_avg<512){
      veloc = -sqrt((-10000.0*((adc_avg/1023.0)-0.5))/rho);
    } else {
      veloc = sqrt((10000.0*((adc_avg/1023.0)-0.5))/rho);
    }
  }

  // same as before but for the second pitot tube
  if (adc_avg2>512-zero_span and adc_avg2<512+zero_span){
  } else{
    if (adc_avg2<512){
      veloc2 = -sqrt((-10000.0*((adc_avg2/1023.0)-0.5))/rho);
    } else {
      veloc2 = sqrt((10000.0*((adc_avg2/1023.0)-0.5))/rho);
    }
  }
  Serial.print(veloc); 
  Serial.print(" ");
  Serial.print(adc_avg);
  Serial.print(" ");
  Serial.print(pressure1);
  Serial.print(" ");
  Serial.print(veloc2);
  Serial.print(" ");
  Serial.print(adc_avg2);
  Serial.print(" ");
  Serial.print(pressure2);
  delay(100);
}
