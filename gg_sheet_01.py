from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file('api_sheet.json')
service = build('sheets', 'v4', credentials=creds)

spreadsheet_id = '10SL6WCt6YPrHUtxzVmsNI1futs-SOi9ebYIn_C641vc'
sheet_name = 'Nhóm Tokutei'
range_name = f'{sheet_name}!B2:B'
result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])

tu_hang = 4  
den_hang = 10 
for i, row in enumerate(values[tu_hang-2:den_hang-1], start=tu_hang):  
    print(f"Row {i}: {row[0]}")
