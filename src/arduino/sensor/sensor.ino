int portMoist = A0;
int portLight = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valueMoist = analogRead(portMoist);
  int valueLight = analogRead(portLight);
  Serial.print(valueMoist);
  Serial.print(';');
  Serial.print(valueLight);
  Serial.print('\n');
}
