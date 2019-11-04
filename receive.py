# Add your Python code here. E.g.
from microbit import *
import radio
radio.on()

while True:
  #since micropython sends numbers as nullbytes, it literally just counts the number of nullbytes, max is 32
    jjj = str(radio.receive_bytes())
    print(jjj.count("x00"))
