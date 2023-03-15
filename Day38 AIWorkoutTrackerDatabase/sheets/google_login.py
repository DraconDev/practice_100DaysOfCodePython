import sheets.sheets_gspread as sheets_gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "../../../_Login/_API/google/service_account.json", scope
)
client = sheets_gspread.authorize(creds)

# Find a workbook by name
sheet = client.open("Name_of_your_Google_Sheet").sheet1

# Extract and print all rows, print row one at a time
rows = sheet.get_all_values()
for row in rows:
    print(row)
