from hw5.records import News, PrivateAd, WeatherForecast
from hw5.user_input import UserInput


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