from google.oauth2 import service_account
from googleapiclient.discovery import build


def login():
    SCOPES = [
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/spreadsheets",
    ]
    SERVICE_ACCOUNT_FILE = "../../../_Login/_API/google/service_account.json"
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    return service
