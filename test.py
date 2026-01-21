from pymodbus.client.sync import ModbusSerialClient            #Pymodbus==2.5.3

# port = 'COM4'  # Windows
port = '/dev/ttyUSB0'  # Ubuntu                      Sudo chmod 666 /dev/ttyUSB0

baudrate = 9600  # Your baud rate
unit_id = 3  # Your unit ID
import logging
import serial
import time

client = ModbusSerialClient(
        method='rtu',
        port=port,
        baudrate=baudrate,
        parity='N',
        stopbits=1,
        bytesize=8,
        timeout=2
    )
result = "NG"
client.connect()

# Check connection
if not client.connect():
    print("Not connect Modbus.")
else:
    print("Connect Modbus.")

# Check signal
####################### address (0: processing, 1: OK, 2: NG, 3: Coil, 4: Top light, 8: signal camera, 9: Bottom light)
for i in range(5):
    client.write_coil(address=i, value=True, unit=unit_id)
    time.sleep(2)

for i in range(8, 10):
    client.write_coil(address=i, value=True, unit=unit_id)
    time.sleep(2)

# Signal capture camera
while True:
    tmp = client.read_coils(address=10, unit=unit_id)
    print(tmp.bits[0])
    client.close()

