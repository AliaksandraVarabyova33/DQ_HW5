from datetime import date


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
        self.days_left = (expiration_date - date.today()).days


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