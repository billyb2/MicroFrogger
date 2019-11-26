import serial, time
s = serial.Serial(
     port='COM11',
    baudrate=115200
 )




while True:
    data = s.readline()
    print(str(data))

    with open('data.txt', 'w') as f:
        f.write(str(data))
