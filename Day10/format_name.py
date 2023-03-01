def format_name(name):

    name_part_list = []

    for word in name.split(" "):
        name_part_list.append(word.lower().capitalize())
    return " ".join(name_part_list)


print(format_name(input('Provide name')))
