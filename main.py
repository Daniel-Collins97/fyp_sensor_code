from network import Sigfox
import socket
import struct
import binascii

def float_to_hex(f):
  x = str(f)
  x = x.encode()
  x = binascii.hexlify(x)
  return x

def hex_to_str(h):
  x = binascii.unhexlify(h)
  x = x.decode()
  return x
  
print(hex_to_str(float_to_hex(1.2345)))

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
​
# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
​
# make the socket blocking
s.setblocking(True)
​
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
​
# send some bytes
my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
# s.send(my_str_as_bytes)

# from LIS2HH12 import LIS2HH12
# import time
# from Pysense import Pysense
# py = Pysense()
# acc = LIS2HH12()


# while True:
#   acceleration = acc.acceleration()
#   print(acceleration)
#   time.sleep(3)