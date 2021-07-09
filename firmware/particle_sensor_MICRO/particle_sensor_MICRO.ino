#include <SoftwareSerial.h>
#include <Wire.h>

SoftwareSerial mySerial(9,8); // RX, TX

byte readMsr[4] = {0x68, 0x01, 0x04, 0x93};
byte startMsr[4] = {0x68, 0x01, 0x01, 0x96};
byte stopMsr[4] = {0x68, 0x01, 0x02, 0x95};
byte autoStop[4] = {0x68, 0x1, 0x20, 0x77};
byte autoStart[4] = {0x68, 0x1, 0x40, 0x57};

void setup() {
  Wire.begin(0x0A);                // join i2c bus with address #10
  Wire.onRequest(requestEvent);
  
  Serial.begin(9600);
  while(!Serial){
    ;
  }
  Serial.println("Serial started...");
  mySerial.begin(9600);
  Serial.println("Software Serial started... waiting 2 seconds...");
  delay(2000);
  Serial.println("Stopping auto send...");
  mySerial.write(autoStop, 4);
  Serial.write(autoStop, 4);
  Serial.println("Starting particle measurement...");
  mySerial.write(startMsr, 4);
}

int test;
const int BUFFER_SIZE = 50;
byte buf[BUFFER_SIZE];
int rlen;
int PM25;
int PM10;

void loop() {
  if(mySerial.available()){
    rlen = mySerial.readBytes(buf, BUFFER_SIZE);
    Serial.print("buffered input: ");
    for(int i = 0; i < rlen; i++){
      Serial.print(buf[i], HEX);
    }
    Serial.println();
  }
  delay(1000);
  readMeasurement();
}

void readMeasurement(){
    mySerial.write(readMsr, 4);
    rlen = mySerial.readBytes(buf, BUFFER_SIZE);
    PM25 = (buf[3] * 256) + buf[4];
    PM10 = (buf[5] * 256) + buf[6];
    Serial.print("Time: ");
    Serial.print(millis());
    Serial.println("ms");
    Serial.print("PM2.5: ");
    Serial.println(PM25, DEC);
    Serial.print("PM10: ");
    Serial.println(PM10, DEC);
}

byte data[4];

void requestEvent(){
  Serial.println("Sending measurements...");
  data[0] = highByte(PM25);
  data[1] = lowByte(PM25);
  data[2] = highByte(PM10);
  data[3] = lowByte(PM10);
  Wire.write(data, 4);
  Serial.write(data, 4);
}
