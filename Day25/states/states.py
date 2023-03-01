import pandas
from PIL import Image, ImageDraw, ImageFont

data = pandas.read_csv('./50_states.csv')
names_of_state = data['state']

answers = []

# Image
image = Image.open("blank_states_img.gif")
print(image.format, image.size, image.mode)


def image_maker(player_guess='', x_coordinate=0, y_coordinate=0):
    global image
    draw = ImageDraw.Draw(image)
    text = player_guess
    font = ImageFont.truetype("arial.ttf", 16)
    text_width, text_height = draw.textsize(text, font=font)
    x = ((image.width) / 2) + int(x_coordinate) - 20
    y = ((image.height) / 2) - int(y_coordinate) - 10
    draw.text((x, y),     text, fill="black", font=font)
    image.save("updated_image.gif")
    image = Image.open("updated_image.gif")
    image.show()


image_maker()


def guess():
    print('Name an American state')
    player_guess = input()

    if len(data.loc[names_of_state == player_guess]) > 0:
        found_index = int(data.index[data['state'] == player_guess][0])

        image_maker(player_guess, data.at[found_index, 'x'],
                    data.at[found_index, 'y'])
        guess()
    else:
        print('Your high score', answers)


guess()
