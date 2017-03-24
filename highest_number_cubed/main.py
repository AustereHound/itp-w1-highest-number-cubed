"""This is the entry point of the program."""

def highest_number_cubed(limit):
    for i in range(limit):
        if i ** 3 <= limit:
            result = i
            continue
    return result
