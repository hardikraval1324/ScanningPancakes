import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


n = int(input("enter number"))
for i in range(n):
     qr = pyqrcode.create("Test Message")
     qr.png(str(i)+".png", scale=8)


# file = ("Freshers List IT and CSE.xlsx")
# b = xlrd.open_workbook(file)
# sheet = b.sheet_by_index(0)
# sheet.cell_value(0, 0)
# print(sheet.rows)

