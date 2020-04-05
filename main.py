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
values = [2.8, 0.2, 1.534]
sensorThreshold = 2.8
seconds = 0

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket​
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# Define function which uses the interrupt alarm and periodically sends the values being stored so that SigFox does not miss any values
def arraySender(alarm):
  global values
  if values:
    s.send(float_to_hex(values[0]))
    del values[0]

# Define the alarm configuration
alarm = Timer.Alarm(arraySender, 15, periodic=True)

# Convert the value to hex so it can be sent to SigFox
def float_to_hex(f):
  x = str(f)
  x = x.encode()
  x = binascii.hexlify(x)
  return x

def check_acceleration():
  x, y, z = acc.acceleration()
  x = abs(x)
  y = abs(y)
  z = abs(z)
  return x, y, z

# Scale the values coming in from the sensor to be more realistic
def value_scale(sensorValue):
  sensorValue = (sensorValue - 1) * 25
  return sensorValue

# Start the interrupt
arraySender(alarm)

# Continously check the sensor to see if the value is above the set threshold or not
while True:
  roll, pitch, yaw = check_acceleration()
  roll = abs(roll)
  pitch = abs(pitch)
  yaw = abs(yaw)
  acceleration = math.sqrt((roll**2) + (pitch**2) + (yaw**2))
  acceleration = value_scale(acceleration)

  # If threshold is broken, add sensor value to the arry
  if acceleration >= sensorThreshold:
    values.append(acceleration)

  # sleep for 2 seconds to allow the sensor to pick up new value
  time.sleep(2)