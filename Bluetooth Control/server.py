import bluetooth

# Define the Bluetooth server socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 1))
server_sock.listen(1)

# Wait for a Bluetooth client to connect
print("Waiting for Bluetooth connection...")
client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

# Loop indefinitely
while True:
    # Receive data from the client
    data = client_sock.recv(1024).decode()

    # Convert the data to an integer
    sensor_data = int(data)

    # Do something with the sensor data
    print("Received sensor data:", sensor_data)
