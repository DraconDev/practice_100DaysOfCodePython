import csv

import pandas

# with open("./226 weather-data.csv") as f:
#     # weather_data = f.readlines()
#     # weather_data = f.readlines()
#     # weather_data = pandas.DataFrame(weather_data)
#     weather_data = pandas.read_csv(f)
#     print(weather_data, weather_data['temp'])

# with open("./226 weather-data.csv") as f:
#     data = csv.reader(f)

#     temps = []
#     for row in data:
#         try:
#             temps.append(int(row[1]))
#         except ValueError:
#             pass
#     print(temps)

with open("./226 weather-data.csv") as f:
    data = pandas.read_csv(f)
    with open('./data.txt', 'w') as file:
        file.write(str(data.to_dict()))

    # avg_temp = sum(temp_list)/len(temp_list)

    print(data, "\n")

    # both works
    # hottest_day = data.loc[data['temp'] == data.temp.max()]
    hottest_day = data[data['temp'] == data.temp.max()]

    # print(data.temp.max())
    # test = data["day"]
    monday = data[data["day"] == "Monday"]

    # print(monday)
    # print(hottest_day)
    # print(data.at[monday, 'temp'])
    print(monday.temp)
