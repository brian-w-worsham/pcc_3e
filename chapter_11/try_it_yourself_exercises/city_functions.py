# 11-1. City, Country: Write a function that accepts two parameters: a city
# name and a country name. The function should return a single string of the
# form City, Country, such as Santiago, Chile. Store the function in a module
# called city_functions.py, and save this file in a new folder so pytest won’t
# try to run the tests we've already written.


def format_city_country(city, country, population=""):
    """Return a string like 'Santiago, Chile'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
