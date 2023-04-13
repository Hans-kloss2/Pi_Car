import bluetooth

# Define the Bluetooth UUIDs for the service and joystick characteristic
SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
JOYSTICK_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

# Get the MAC address of the ESP32
esp32_address = "A8:03:2A:13:01:B2"  # Replace with the MAC address of the ESP32


# Create a Bluetooth socket and connect to the ESP32
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_address, 1))

# Send a command to read the joystick values
command = bytes([0x01])
sock.send(command)

# Receive the joystick values from the ESP32
data = sock.recv(1024)
print(f"Joystick values: {data}")

# Close the Bluetooth socket
sock.close()
