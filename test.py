from pymodbus.client.sync import ModbusSerialClient

port = 'COM4'  # Your COM port
baudrate = 9600  # Your baud rate
unit_id = 3  # Your unit ID
import logging
import serial
import time

############################### Check port availability
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

# try:
#     # Kiểm tra cổng serial trước
#     ser = serial.Serial(port, baudrate, timeout=1)
#     ser.close()
#     print(f"Cổng {port} có thể truy cập được")
    
#     # Thử kết nối Modbus
#     client = ModbusSerialClient(
#         method='rtu',
#         port=port,
#         baudrate=baudrate,
#         parity='N',
#         stopbits=1,
#         bytesize=8,
#         timeout=2
#     )
    
#     if client.connect():
#         print("Kết nối Modbus thành công!")
#         client.close()
#     else:
#         print("Không thể kết nối Modbus!")
        
# except serial.SerialException as e:
#     print(f"Lỗi cổng serial: {e}")
# except Exception as e:
#     print(f"Lỗi không xác định: {e}")

############# Run
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
client.write_coil(address=0, value=True, unit=unit_id)
time.sleep(2)
if result == "OK":
    client.write_coil(address=0, value=False, unit=unit_id)
    client.write_coil(address=1, value=True, unit=unit_id)

if result == "NG":
    client.write_coil(address=0, value=False, unit=unit_id)
    client.write_coil(address=2, value=True, unit=unit_id)
    client.write_coil(address=3, value=True, unit=unit_id)

