import Levenshtein


def authentic_brands(copy_values):
    if len(copy_values) == 4:
        if ".com" in copy_values[2] or ".co" in copy_values[2]:
            copy_values[2] = copy_values[2].split(".co")[0].split("//")[1].replace(".", "")
        elif ".gr" in copy_values[2]:
            copy_values[2] = copy_values[2].split(".gr")[0].split("//")[1].replace(".", "")
        elif ".org" in copy_values[2]:
            copy_values[2] = copy_values[2].split(".org")[0].split("//")[1].replace(".", "")
        elif ".net" in copy_values[2]:
            copy_values[2] = copy_values[2].split(".net")[0].split("//")[1].replace(".", "")

        similarity_ratio = Levenshtein.jaro(copy_values[1].lower(), copy_values[2])

    elif len(copy_values) == 5:
        if ".com" in copy_values[3] or "co" in copy_values[2]:
            copy_values[3] = copy_values[3].split(".co")[0].split("//")[1].replace(".", "")
        elif ".gr" in copy_values[3]:
            copy_values[3] = copy_values[3].split(".gr")[0].split("//")[1].replace(".", "")
        elif ".org" in copy_values[3]:
            copy_values[3] = copy_values[3].split(".org")[0].split("//")[1].replace(".", "")
        elif ".net" in copy_values[3]:
            copy_values[3] = copy_values[3].split(".net")[0].split("//")[1].replace(".", "")

        similarity_ratio = Levenshtein.jaro(copy_values[2].lower(), copy_values[3])

    elif len(copy_values) == 6:
        if ".com" in copy_values[4] or "co" in copy_values[2]:
            copy_values[4] = copy_values[4].split(".co")[0].split("//")[1].replace(".", "")
        elif ".gr" in copy_values[4]:
            copy_values[4] = copy_values[4].split(".gr")[0].split("//")[1].replace(".", "")
        elif ".org" in copy_values[4]:
            copy_values[4] = copy_values[4].split(".org")[0].split("//")[1].replace(".", "")
        elif ".net" in copy_values[4]:
            copy_values[4] = copy_values[4].split(".net")[0].split("//")[1].replace(".", "")

        similarity_ratio = Levenshtein.jaro(copy_values[3].lower(), copy_values[4])

    return similarity_ratio
