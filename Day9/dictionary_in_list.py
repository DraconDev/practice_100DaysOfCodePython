travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_name, visit_number, list_of_cities_visited):
    travel_log.append({"country": country_name,
                       "visits": visit_number, "cities": list_of_cities_visited})
    # print([*travel_log, 1])
    # travel_log[*travel_log, {"country": country_name,
    #                             "visits": visit_number, "cities": list_of_cities_visited}]


    # 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
