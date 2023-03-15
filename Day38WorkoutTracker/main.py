import json
import os

import gspread
import pandas as pd


def main():
    gc = gspread.service_account(
        filename="../../../_Login/_API/google/service_account.json"
    )
    worksheet = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1ltmNP4JDjdIesBQo_YrSlEua76vVPNtox5dSjc3afr4/"
    ).sheet1

    dataFrame = pd.DataFrame(worksheet.get_all_records())

    if not os.path.exists("./data"):
        os.mkdir("./data/")
    pd.DataFrame.to_json(dataFrame, "./data/sheet.json")
    pass


if __name__ == "__main__":
    main()
