const int NSR = 2;
const int NSY = 3;
const int NSG = 4;
const int EWR = 5;
const int EWY = 6;
const int EWG = 7;
const int Button = 8;
const int Button2 = 9;
int state = 1;

void setup()
{
  pinMode(NSR, OUTPUT);
  pinMode(NSY, OUTPUT);
  pinMode(NSG, OUTPUT);
  pinMode(EWR, OUTPUT);
  pinMode(EWY, OUTPUT);
  pinMode(EWG, OUTPUT);
  pinMode(Button, INPUT);
  pinMode(Button2, INPUT);
  Serial.begin(9600);
}




void loop()
{
  boolean emergency = digitalRead(Button);
  boolean night = digitalRead(Button2);
  Serial.print(emergency);  Serial.print(" "); Serial.println(night);
  if(state==1)  
  {
    if(emergency)
    {
      digitalWrite(NSR, HIGH);
      digitalWrite(NSY, LOW);
      digitalWrite(NSG, LOW);
      digitalWrite(EWR, HIGH);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      state = 2;
      delay(2000);
    }
    else if(night)
    {
      digitalWrite(NSR, HIGH);
      digitalWrite(NSY,LOW);
      digitalWrite(NSG, LOW);
      digitalWrite(EWR, LOW);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      delay(200);
      digitalWrite(NSR, LOW);
      digitalWrite(EWY, HIGH);
      delay(200);
      state = 1;
    }
      else
    {
      digitalWrite(NSR, LOW);
      digitalWrite(NSG, HIGH);
      digitalWrite(EWR, HIGH);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      state = 2;
      delay(2000);
    }
  }
    
  else if(state==2)
  {
    if (emergency)
    {
      digitalWrite(NSR, HIGH);
      digitalWrite(NSY, LOW);
      digitalWrite(NSG, LOW);
      digitalWrite(EWR, HIGH);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      state = 3;
      delay(1000);
    }
    else{
    digitalWrite(NSR, LOW);
    digitalWrite(NSY, HIGH);
    digitalWrite(NSG, LOW);
    digitalWrite(EWR, HIGH);
    digitalWrite(EWY, LOW);
    digitalWrite(EWG, LOW);
    state = 3;
    delay(1000);
    }
  }
  else if(state==3)
  {
    if(emergency)
    {
      digitalWrite(NSR, HIGH);
      digitalWrite(NSY, LOW);
      digitalWrite(NSG, LOW);
      digitalWrite(EWR, HIGH);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      state = 4;
      delay(2000);
    }
    else
    {
    digitalWrite(NSR, HIGH);
    digitalWrite(NSY, LOW);
    digitalWrite(NSG, LOW);
    digitalWrite(EWR, LOW);
    digitalWrite(EWY, LOW);
    digitalWrite(EWG, HIGH);
    state = 4;
    delay(2000);
  }
  }
  else if(state==4)
  {
    if(emergency)
    {
      digitalWrite(NSR, HIGH);
      digitalWrite(NSY, LOW);
      digitalWrite(NSG, LOW);
      digitalWrite(EWR, HIGH);
      digitalWrite(EWY, LOW);
      digitalWrite(EWG, LOW);
      state = 1;
      delay(1000);
    }
    else{
    digitalWrite(NSR, HIGH);
    digitalWrite(NSY, LOW);
    digitalWrite(NSG, LOW);
    digitalWrite(EWR, LOW);
    digitalWrite(EWY, HIGH);
    digitalWrite(EWG, LOW);
    state = 1;
    delay(1000);
  }
}
}
