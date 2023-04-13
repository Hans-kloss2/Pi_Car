#include <BluetoothSerial.h>

// Define the address of the Raspberry Pi 4
String server_address = "E4:5F:01:C6:44:9B";  // Replace with your Raspberry Pi 4's Bluetooth address
// AC:67:B2:35:BF:9A
BluetoothSerial SerialBT;

////////////////////////////////////////////////////////////////////////////
const int JOYSTICK_X_PIN = 39;       // Connect VRX to A0
const int JOYSTICK_Y_PIN = 35;       // Connect VRY to A1
////////////////////////////////////////////////////////////////////////////





void setup() {
  // Start the SerialBT module
  SerialBT.begin("JoyStick_Controler");  // Set the name of the ESP32 Bluetooth device

  // Connect to the Raspberry Pi 4
  SerialBT.connect(server_address);

  Serial.begin(115200);

  // Wait for a short amount of time before sending the first data
  delay(1000);
}

void loop() {
  int x = analogRead(JOYSTICK_X_PIN);
  int y = analogRead(JOYSTICK_Y_PIN);

  Serial.println("X: ");
  Serial.println(x);
  Serial.println("\tY: ");
  Serial.println(y);

  // Format the data as a string
  String data = String(x, y);
  // Send the data over Bluetooth
  SerialBT.print(data);

  // Wait for a short amount of time before sending the next data
  delay(100);
}
