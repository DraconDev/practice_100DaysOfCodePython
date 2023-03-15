def update_cell(
    service: str,
    spreadsheet_id: str,
    range_: str,
    value_range_body,
    value_input_option="USER_ENTERED",
):
    request = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption=value_input_option,
            body=value_range_body,
        )
    )
    response = request.execute()
    # pprint(response)
    return response


def batch_update_cell(
    service: str,
    spreadsheet_id: str,
    value_range_body,
):
    request = (
        service.spreadsheets()
        .values()
        .batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=value_range_body,
        )
    )
    response = request.execute()
    # pprint(response)
    return response


def get_cell(
    service: str,
    spreadsheet_id: str,
    range_: str,
):
    request = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id,
            range=range_,
        )
    )
    response = request.execute()

    return response


def format_range(cell: str, sheet="Sheet1!"):
    return sheet + cell

    # spreadsheet_id = "1ltmNP4JDjdIesBQo_YrSlEua76vVPNtox5dSjc3afr4"
    # service = login()
    # data = {"values": [[10]]}
    # # batch_data = {
    # #     "data": [{"range": format_range("A1:A10"), "values": [6]}],
    # #     # "valueInputOption": "USER_ENTERED",
    # # }
    # value_range_body = {
    #     "valueInputOption": "USER_ENTERED",
    #     "data": [{"range": format_range("C8"), "values": [[10, 10], ["a", "b"]]}],
    # }
    # # update_sheet_value(service, spreadsheet_id, "A1", 10)
    # # update_cell(service, spreadsheet_id, format_range("A7"), data)
    # batch_update_cell(service, spreadsheet_id, value_range_body)
    # # cell_value = get_cell(service, spreadsheet_id, format_range("B3"))
    # # update_sheets(service, spreadsheet_id)
