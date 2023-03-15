def open_sheet_as_database(
    service_file_location="../../../_Login/_API/google/service_account.json",
    sheet_link="https://docs.google.com/spreadsheets/d/1ltmNP4JDjdIesBQo_YrSlEua76vVPNtox5dSjc3afr4/",
    sheet_name="sheet1",
):
    """
    This function opens a Google Sheet as a database. It takes three arguments:
    service_file_location (a string containing the path to the service account file),
    sheet_link (a string containing the link to the Google Sheet) and sheet_name (a string containing the name of the sheet).
    It uses gspread to login to the sheets and get all data in a dataframe, which is then returned."""

    # login to sheets and get all data in dataframe
    gc = gspread.service_account(filename=service_file_location)
    worksheet = gc.open_by_url(sheet_link)[sheet_name]
    data_frame = pd.DataFrame(worksheet.get_all_records())

    return [data_frame, worksheet]


def update_sheets(data_to_append, dataframe, worksheet):
    # update data
    dataframe_to_append = pd.DataFrame(data_to_append, index=[0])
    df = pd.concat([dataframe, dataframe_to_append])
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    # save data
    if not os.path.exists("./data"):
        os.mkdir("./data/")
    df.reset_index(drop=True).to_json("./data/sheet.json")
