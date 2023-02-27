import pandas

with open('./228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv') as f:
    data = pandas.read_csv(f)

    gray = 0
    cinnamon = 0
    black = 0
    fur_color = data['Primary Fur Color']
    for color in fur_color:
        if color == "Gray":
            gray += 1
        if color == "Cinnamon":
            cinnamon += 1
        if color == "Black":
            black += 1
        else:
            pass

    data = pandas.DataFrame(
        {"Color": ["Black", "Cinnamon", 'Gray'], 'count': [black, cinnamon, gray]})

    data.to_csv('./squirrel_data.csv')
