const int pwm=3;

int my_map(float value, float lower_voltage, float upper_voltage, int lower_dc, int upper_dc)
{
  int y;
  float m = (upper_dc-lower_dc)/(upper_voltage-lower_voltage);
  float b = upper_dc-lower_dc - m*upper_voltage;
  y = m*value + b ;
  return (y);
}


void setup() {
  // put your setup code here, to run once:

}


void loop() {
   float pr = analogRead(A0);
  float voltage = pr*(5.0/1023);  
  int dc = my_map(voltage, 2.90, 5.00, 0, 255);
  analogWrite (pwm, dc); 
  
}
