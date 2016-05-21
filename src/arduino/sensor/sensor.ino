int portMoist = A0;
int portLight = A1;
int valueMoist = 0;
int valueLight = 0;
char datastring[18] = {0};
String received;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    received = Serial.readString();
    
    valueMoist = analogRead(portMoist);
    valueLight = analogRead(portLight);
    sprintf(datastring, "%02X;%02X", valueMoist, valueLight);
    Serial.println(datastring);
  }
}
