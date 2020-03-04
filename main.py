from network import Sigfox
import socket
​
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
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# from LIS2HH12 import LIS2HH12
# import time
# from Pysense import Pysense
# py = Pysense()
# acc = LIS2HH12()


# while True:
#   acceleration = acc.acceleration()
#   print(acceleration)
#   time.sleep(3)