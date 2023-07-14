#include <SoftwareSerial.h>
#include "./TinyWireS.h"

#define I2C_SLAVE_ADDRESS 0x10
SoftwareSerial mySerial(3, 4);  //rx, tx
char sensor_output[32];
char i2c_output[4];
unsigned int pm25;
unsigned int pm10;

int index = 0;

void setup() {
  // i2c
  TinyWireS.begin(I2C_SLAVE_ADDRESS);
  TinyWireS.onRequest(requestEvent);
  // uart
  pinMode(3, INPUT);
  pinMode(4, OUTPUT);
  mySerial.begin(9600);
  delay(500);
  mySerial.write(0x68014057);  // ask the sensor to send data asyncronously
  // LED
  pinMode(1, OUTPUT);
}

void loop() {

  TinyWireS_stop_check();  // need to call periodically

  if (mySerial.available()) {
    // brute force shift all data to left one char
    for (int i = 0; i < 32; i++) {
      sensor_output[i] = sensor_output[i + 1];
    }
    // place new byte on trailing end of buffer
    sensor_output[31] = mySerial.read();
  }

  if ((sensor_output[0] == 0x42) & (sensor_output[1] == 0x4d)) {
    digitalWrite(1, HIGH);
    i2c_output[0] = sensor_output[6];
    i2c_output[1] = sensor_output[7];
    i2c_output[2] = sensor_output[8];
    i2c_output[3] = sensor_output[9];
    delay(500);
    digitalWrite(1, LOW);
  }
}

void requestEvent() {
  for (int i = 0; i < 4; i++) {
    TinyWireS.send(i2c_output[i]);
  }
}
