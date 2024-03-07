import httplib2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

COLUMN_PRICE = 2
COLUMN_QUANTITIES = 3
COLUMN_COST = 4

# Путь к файлу ключа и ID таблицы
credentials_file = "key_json.json"
spreadsheet_id = "1-lq_N6qYwnHGahshjRhn8Myx8n0fJtKXBmpaAJsVy9M"

# Область доступа
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

try:
    # Авторизация
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file, scope
    )
    client = gspread.authorize(credentials)
    httpAuth = credentials.authorize(httplib2.Http())

    # Имя таблицы
    spreadsheet_name = "Pyt_T"
    spreadsheet = client.open(spreadsheet_name)
    SHEET = spreadsheet.sheet1

except Exception as e:
    print("Ошибка при авторизации: ", e)
    exit(1)
