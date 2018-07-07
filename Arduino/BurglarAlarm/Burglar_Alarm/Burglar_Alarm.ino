const int button = 2;
const int led = 4;

void setup ()
{
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(led, OUTPUT);
}

void loop()
{
  boolean buttonPressed = digitalRead(button);
  if (buttonPressed)
  {
    Serial.println("Button is not pressed");
    digitalWrite(led, LOW);
  }
  else
  {
    Serial.println("Button is pressed");
    digitalWrite(led, HIGH);
    delay(35);
    digitalWrite(led, LOW);
    delay(35);
  }
}
  
  
