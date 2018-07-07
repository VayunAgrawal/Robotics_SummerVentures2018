const int pwm=3;

int my_map(float value, float lower_voltage, float upper_voltage, int lower_dc, int upper_dc)
{
  
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
 // float pr = analogRead(A0);
  //float prv = pr*(5.0/1023);
  //Serial.println(pr);
  for(int i; i<=255; i++){
     analogWrite(pwm, i);
  delay(1);
  }
  for(int i=254; i>=0; i--){
    analogWrite(pwm, i);
    delay(1);
  }
 
 
}
