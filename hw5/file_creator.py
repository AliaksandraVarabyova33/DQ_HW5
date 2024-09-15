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
