def get_foramt_number(number):
    if number < 10:
        return "00" + str(number)
    elif number < 100:
        return "0" + str(number)
    else:
        return str(number)


if __name__ == "__main__":
    print(get_foramt_number(1))
    print(get_foramt_number(10))
    print(get_foramt_number(100))
