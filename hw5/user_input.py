from datetime import date


class UserInput:
    @staticmethod
    def record_type_input():
        return int(input("Select type of data:\nEnter 1 for News, 2 for PrivateAd, 3 for Weather Forecast"))

    @staticmethod
    def text_input():
        return input("Enter your text")

    @staticmethod
    def city_input():
        return input("Enter the city")

    @staticmethod
    def expiration_date_input():
        date_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        return date(year, month, day)

    @staticmethod
    def weather_parameters_input():
        weather_parameters = []
        weather_parameters.append(input("It's rainy: enter true or false?"))
        weather_parameters.append(input("It's sunny: enter or false?"))
        weather_parameters.append(input("It's windy: enter or false?"))
        return weather_parameters