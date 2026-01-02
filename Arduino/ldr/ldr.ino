int ldrPin = A0;
int redLED = 8;
int lightValue;

void setup() {
  pinMode(redLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  lightValue = analogRead(ldrPin);
  Serial.println(lightValue);

  if (lightValue >32) {
    digitalWrite(redLED, HIGH);
  
  } else {
    digitalWrite(redLED, LOW);
   
  }
  delay(50);
}