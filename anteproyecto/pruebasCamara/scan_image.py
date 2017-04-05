#!/usr/bin/python
from qrtools import QR
myCode = QR()
print myCode.decode_webcam()