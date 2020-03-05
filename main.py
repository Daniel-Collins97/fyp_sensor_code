from network import Sigfox
import socket
​
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket​
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
s.send("000102030405060708090A0B")
print("FINSIHED")

# from network import Sigfox
# import socket
# from lib.LIS2HH12 import LIS2HH12
# import time
# from lib.Pysense import Pysense
# import math
# import binascii
# py = Pysense()
# acc = LIS2HH12()
# minLimit = 2

# # init Sigfox for RCZ1 (Europe)
# sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# # create a Sigfox socket​
# s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# # make the socket blocking
# s.setblocking(True)

# # configure it as uplink only
# s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# def checkAcceleration():
#   x, y, z = acc.acceleration()
#   x = abs(x)
#   y = abs(y)
#   z = abs(z)
#   return x, y, z

# while True:
#   roll, pitch, yaw = checkAcceleration()
#   roll = abs(roll)
#   pitch = abs(pitch)
#   yaw = abs(yaw)
  
#   # print('roll: ', roll)
#   # print('pitch: ', pitch)
#   # print('yaw: ', yaw)
#   acceleration = math.sqrt((roll**2) + (pitch**2) + (yaw**2))
#   print('acceleration = ', acceleration)
#   print('--------------------\n\n')
#   if acceleration > minLimit:
#     # send some bytes
#     payload = binascii.hexlify(b'GREATER')
#     s.send("000102030405060708090A0B")
#     print("GREATER")
#   time.sleep(0.5)