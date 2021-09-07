import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


n = int(input("enter number"))
for i in range(n):
     qr = pyqrcode.create("This not ")
     qr.png("check.png", scale=8)


