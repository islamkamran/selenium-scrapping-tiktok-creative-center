# Cleaning the Links Removing the Extra part
# def clean_links(values):
#     if len(values) == 4:
#         values[2] = values[2].split(".com")[0] + ".com/"
#     elif len(values) == 5:
#         values[3] = values[3].split(".com")[0] + ".com/"
#     elif len(values) == 6:
#         values[4] = values[4].split(".com")[0] + ".com/"

#     return values


def clean_links(values):
    if len(values) == 4:
        if ".com" in values[2]:
            values[2] = values[2].split(".com")[0] + ".com/"
        elif ".co" in values[2]:
            values[2] = values[2].split(".co")[0] + ".co/"
        elif ".gr" in values[2]:
            values[2] = values[2].split(".gr")[0] + ".gr/"
        elif ".org" in values[2]:
            values[2] = values[2].split(".org")[0] + ".org/"
        elif ".net" in values[2]:
            values[2] = values[2].split(".net")[0] + ".org/"

    elif len(values) == 5:
        if ".com" in values[3]:
            values[3] = values[3].split(".com")[0] + ".com/"
        elif ".co" in values[3]:
            values[3] = values[3].split(".co")[0] + ".co/"
        elif ".gr" in values[3]:
            values[3] = values[3].split(".gr")[0] + ".gr/"
        elif ".org" in values[3]:
            values[3] = values[3].split(".org")[0] + ".org/"
        elif ".net" in values[3]:
            values[3] = values[3].split(".net")[0] + ".net/"

    elif len(values) == 6:
        if ".com" in values[4]:
            values[4] = values[4].split(".com")[0] + ".com/"
        elif ".co" in values[4]:
            values[4] = values[4].split(".co")[0] + ".co/"
        elif ".gr" in values[4]:
            values[4] = values[4].split(".gr")[0] + ".gr/"
        elif ".org" in values[4]:
            values[4] = values[4].split(".org")[0] + ".org/"
        elif ".net" in values[4]:
            values[4] = values[4].split(".net")[0] + ".net/"

    return values
