#include <BluetoothSerial.h>

// Define the address of the Raspberry Pi 4
String server_address = "E4:5F:01:C6:44:9B";  // Replace with your Raspberry Pi 4's Bluetooth address

BluetoothSerial SerialBT;

void setup() {
  // Start the SerialBT module
  SerialBT.begin("ESP32");  // Set the name of the ESP32 Bluetooth device

  // Connect to the Raspberry Pi 4
  SerialBT.connect(server_address);

  // Wait for a short amount of time before sending the first data
  delay(1000);
}

void loop() {
  // Read some data from a sensor or input pin
  int sensor_data = 420;  // Replace with your sensor reading code

  // Format the data as a string
  String data = String(sensor_data);

  // Send the data over Bluetooth
  SerialBT.print(data);

  // Wait for a short amount of time before sending the next data
  delay(100);
}
