import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
import jwt
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("test sheet").sheet1

data = sheet.get_all_records() #getting all the values from Spreedsheet
col1 = sheet.col_values(2)
col = sheet.col_values(6)
pprint([col1, col])
for i in range(len(data)):
     encoded_jwt = jwt.encode({"Name": data[i]["Name"], "U_Code": data[i]["U_Code"] , "Contact No": data[i]["Contact No"]}, "H2O2002", algorithm="HS256")
     pprint(encoded_jwt)
     qr = pyqrcode.create(encoded_jwt)
     qr.png(str(i)+".png", scale=8)
     decoded = jwt.decode(encoded_jwt, "H2O2002", algorithms=["HS256"])
     pprint(decoded)

"""
 logic to update the cell 
   if(ture):
       sheet.update_cell(x,y, "Checked IN")
   else: 
      sheet.update_cell(x,y, "empty string")
"""