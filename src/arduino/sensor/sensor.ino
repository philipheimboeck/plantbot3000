int portMoist = A0;
int portLight = A1;
int valueMoist = 0;
int valueLight = 0;
char datastring[18] = {0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  valueMoist = analogRead(portMoist);
  valueLight = analogRead(portLight);
  sprintf(datastring, "%02X;%02X", valueMoist, valueLight);
  Serial.println(datastring);
  delay(1000);
}
