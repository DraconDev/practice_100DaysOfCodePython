import datetime as dt

import pandas

now = dt.datetime.now()


data = pandas.read_csv("./data/birthdays.csv")
# * Strip extra whitespace
str_cols = data.select_dtypes(include=['object']).columns
data[str_cols] = data[str_cols].apply(lambda x: x.str.strip())
data

print(data)

for i, row in data.iterrows():
    if row.month == now.month and row.day == now.day:
        pass
        # test = {i: row for i, row in data.iterrows()}

        # test = year

print(now)
