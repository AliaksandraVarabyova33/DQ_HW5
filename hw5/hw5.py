from datetime import date, datetime


class Record:
    def __init__(self, text):
        self.text = text


class News(Record):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.dt = date.today()


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = expiration_date
        self.days_left = expiration_date - date.today()


class WeatherForecast(Record):
    def __init__(self, is_rainy, is_sunny, is_windy, city):
        super().__init__("Today the following weather is expected:\nRainy: " + is_rainy + "\nWindy: " + is_windy + "\nSunny: " + is_sunny)
        self.city = city
        self.dt = date.today()
        if is_rainy == 'true' and is_windy == 'true' and is_sunny == 'false':
            self.weather_rating = 1
        elif is_rainy == 'true' and is_windy == 'false' and is_sunny == 'false':
            self.weather_rating = 2
        elif is_rainy == 'false' and is_windy == 'true' and is_sunny == 'false':
            self.weather_rating = 3
        elif is_rainy == 'false' and is_windy == 'true' and is_sunny == 'true':
            self.weather_rating = 4
        elif is_rainy == 'false' and is_windy == 'false' and is_sunny == 'false':
            self.weather_rating = 5
        else:
            self.weather_rating = 6


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


class RecordCreator:
    @staticmethod
    def create_record(record_type):
        if record_type == 1:
            return News(UserInput.text_input(), UserInput.city_input())
        elif record_type == 2:
            return PrivateAd(UserInput.text_input(), UserInput.expiration_date_input())
        else:
            weather_parameters = UserInput.weather_parameters_input()
            return WeatherForecast(weather_parameters[0], weather_parameters[1], weather_parameters[2], UserInput.city_input())


class FileCreator:
    def __init__(self):
        self.file = open("newsfeed.txt", "a")

    def add_record_to_file(self, record):
        if record.__class__.__name__ == "News":
            self.file.write("News:\n" + record.text + "\n" +record.city + ", " + str(record.dt) + "\n--------------------\n\n")
        elif record.__class__.__name__ == "PrivateAd":
            self.file.write("PrivateAd:\n" + record.text + "\n" + "Actual till: " + str(record.expiration_date) + ", days left: " + str(record.days_left) + "\n--------------------\n\n")
        else:
            self.file.write("Weather Forecast:\n" + record.text + "\n" + "Weather rating: " + str(record.weather_rating) + "\n" + record.city + ", " + str(record.dt) + "\n--------------------\n\n")


class Main:
    file_creator = FileCreator()
    file_creator.add_record_to_file(RecordCreator().create_record(UserInput().record_type_input()))
    file_creator.add_record_to_file(RecordCreator().create_record(UserInput().record_type_input()))
    file_creator.add_record_to_file(RecordCreator().create_record(UserInput().record_type_input()))







