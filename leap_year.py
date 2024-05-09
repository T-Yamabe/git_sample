def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def __main__():
    years = [1900, 2000, 2016, 1987]

    for year in years:
        if is_leap_year(year):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")

if __name__ == "__main__":
    __main__()