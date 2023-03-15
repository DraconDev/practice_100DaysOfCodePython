import os

import gspread
import pandas as pd


class InitializeSheets:
    """docstring for InitializeSheets."""

    def __init__(
        self,
    ):
        super(InitializeSheets, self).__init__()
        self.service_file_location = "../../../_Login/_API/google/service_account.json"
        self.sheet_link = "https://docs.google.com/spreadsheets/d/1ltmNP4JDjdIesBQo_YrSlEua76vVPNtox5dSjc3afr4/"

        self.sheet_name = "Sheet1"

    def open_sheet_as_database(self):
        # login to sheets and get all data in dataframe
        gc = gspread.service_account(filename=self.service_file_location)
        self.worksheet = gc.open_by_url(self.sheet_link).worksheet(self.sheet_name)
        self.dataframe = pd.DataFrame(self.worksheet.get_all_records())

    def update_sheets(
        self,
        data_to_append,
    ):
        # update data
        data_to_append = pd.DataFrame(data_to_append, index=[0])
        df = pd.concat([self.dataframe, data_to_append])
        self.worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        # save data
        if not os.path.exists("./data"):
            os.mkdir("./data/")
        df.reset_index(drop=True).to_json("./data/sheet.json")


