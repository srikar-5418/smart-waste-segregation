import serial
ser=serial.Serial()
ser.port='COM7'
ser.close()
ser.open()
ser.baudrate=9600
ser.write(str.encode(input()))

ser.close()
