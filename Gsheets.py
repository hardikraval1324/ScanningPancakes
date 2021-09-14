import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
import jwt
import json
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("test sheet").sheet1
data = sheet.get_all_records() #getting all the values from Spreedsheet
name = sheet.col_values(2)
email = sheet.col_values(8)
# loop for printing name in json format
def making_listToJson():
     res = []
     for i in range(1, len(data) + 1):
          temp = {"name": name[i],
                  "email": email[i]}
          res.append(temp)
     print(res)
     jsonFile = open("reciepents.json", "w")
     jsonFile.write(json.dumps(res))
     jsonFile.close()

def making_qr():
     for i in range(len(data)):
          encoded_jwt = jwt.encode(
               {"Name": data[i]["Name"], "U_Code": data[i]["U_Code"], "Contact No": data[i]["Contact No"]},
               "ef61152cce1d66d77cc0fe52d4996271ec9d74f33c891c23c2fa445b1a3b2f15780a1b35848a3a814e11144fe339eba7f8d049fb892f42121715c454d323b5c4",
               algorithm="HS256")
          pprint(encoded_jwt)
          qr = pyqrcode.create(encoded_jwt)
          qr.png(str(i+1) + ".png", scale=8)
          decoded = jwt.decode(encoded_jwt, "ef61152cce1d66d77cc0fe52d4996271ec9d74f33c891c23c2fa445b1a3b2f15780a1b35848a3a814e11144fe339eba7f8d049fb892f42121715c454d323b5c4", algorithms=["HS256"])
          pprint(decoded)


making_listToJson()


