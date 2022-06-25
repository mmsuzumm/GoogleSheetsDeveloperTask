import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

class SheetAccess:
    def __init__(self):
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]  # Указываем параметры для работы с таблицей
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')  # Указываем путь до файла с нашими реквизитами

        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        # Собираем наши реквизиты и параметры

        SAMPLE_SPREADSHEET_ID = '17z6GdQSBzqJuTYY2olyZnCbOHjAv0k_axgEzu7esupY'  # указываем таблицу в google sheets
        SAMPLE_RANGE_NAME = 'TestList'  # указываем лист в таблице

        service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

        #  Далее вызов API
        self.data = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    def get_sheet_data(self) -> None:
        print('Start show table')
        for value in self.data.get('values'):
            print(value)
        print('End show table', end='\n\n')

    def take_max_line_a(self) -> int:
        print(self.data.get('values'))
        return len(self.data.get('values'))  # Получаем наибольшее значение строки A


new_sheet = SheetAccess()
new_sheet.get_sheet_data()
