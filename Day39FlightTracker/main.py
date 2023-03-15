# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import InitializeSheets
from flight_search import FlightSearch


def main():
    sheets = InitializeSheets()
    df = sheets.open_sheet_as_database()
    flight_search = FlightSearch()
    flight_data = flight_search.get_flight()


if __name__ == "__main__":
    main()
