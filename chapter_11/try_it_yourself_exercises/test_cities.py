from city_functions import format_city_country


# Create a file called test_cities.py that tests the function you just wrote.
# Write a function called test_city_country() to verify that calling your
# function with values such as 'santiago' and 'chile' results in the correct
# string. Run the test, and make sure test_city_country() passes.


def test_city_country():
    """Do names like 'Santiago, Chile' work?"""
    formatted_string = format_city_country('santiago', 'chile')
    assert formatted_string == 'Santiago, Chile'


def test_city_country_population():
    """Do names like 'Santiago, Chile - population 5000000' work?"""
    formatted_string = format_city_country('santiago', 'chile', 5_000_000)
    assert formatted_string == 'Santiago, Chile - population 5000000'
