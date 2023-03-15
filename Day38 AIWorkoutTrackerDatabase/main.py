import datetime

from python_oop_sheets import InitializeSheets
from workout_tracker import analyze_input


def main():
    # vars
    instruction = "Send back exercise type in one word"
    text_input = "I swam today at 16:50 for an hour"
    exercise_data = {
        "Date": str(datetime.date.today()),
        "Time": "15:00:00",
        "Exercise": analyze_input(text_input, instruction),
        "Duration_in_minutes": 60,
        "Calories_burned": 1000,
    }
    sheets = InitializeSheets()
    sheets.open_sheet_as_database()
    sheets.update_sheets(exercise_data)


if __name__ == "__main__":
    main()
