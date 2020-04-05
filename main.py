from network import Sigfox
from machine import Timer
import socket
import struct
import binascii
from lib.LIS2HH12 import LIS2HH12
from lib.Pysense import Pysense
import math
import time

py = Pysense()
acc = LIS2HH12()
values = []
minLimit = 2 #Value in g-force

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket​
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

def float_to_hex(f):
  x = str(f)
  x = x.encode()
  x = binascii.hexlify(x)
  return x

def hex_to_str(h):
  x = binascii.unhexlify(h)
  x = x.decode()
  return x

def checkAcceleration():
  x, y, z = acc.acceleration()
  x = abs(x)
  y = abs(y)
  z = abs(z)
  return x, y, z

while True:
  roll, pitch, yaw = checkAcceleration()
  roll = abs(roll)
  pitch = abs(pitch)
  yaw = abs(yaw)
  acceleration = math.sqrt((roll**2) + (pitch**2) + (yaw**2))
  print("Acceleration: ", acceleration)
  if acceleration > minLimit:
    values.append(acceleration)
    print("Values: ", values)
  time.sleep(2)

print("float to hex (1.234): ", float_to_hex(1.234))
hex_value = float_to_hex(1.234)
print("Hex to string (1.234): ", hex_to_str(hex_value))

# send some bytes
s.send(float_to_hex(2.321))
print("FINISHED")
