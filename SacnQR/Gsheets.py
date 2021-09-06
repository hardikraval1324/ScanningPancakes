import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("test sheet").sheet1

data = sheet.get_all_records() #getting all the values from Spreedsheet
col = sheet.col_values(6)
pprint(col)

"""
 
 logic to update the cell 
   if(ture):
       sheet.update_cell(x,y, "Checked IN")
   else: 
      sheet.update_cell(x,y, "empty string")
"""