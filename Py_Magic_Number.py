import serial
from serial.tools import list_ports
import time
import numpy as np

timestamp = int(time.time())
timestamp = np.int32(timestamp)
print(type(timestamp))

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = None
ser.write_timeout = None
ser.port = list_ports.comports()[0].device
ser.open()

ser.write(timestamp)
return_value = ser.readline()
print(return_value)





