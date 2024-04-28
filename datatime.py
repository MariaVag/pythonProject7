from datetime import datetime

class SuperData(datetime):
    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)


    def get_season(self, months):
        if months in [12, 1, 2]:
            return 'Winter'
        if months in [3, 4, 5]:
            return 'Spring'
        if months in [6, 7, 8]:
            return 'Summer'
        if months in [9, 10, 11]:
            return 'Autumn'
        else:
            return None

    def get_time_of_day(self, hour):
        if hour <= 5 or hour >= 23:
            return 'Сейчас ночь'
        elif hour >= 6 and hour <= 11:
            return 'Сейчас утро'
        elif hour >= 12 and hour <= 17:
            return 'Сейчас вечер'
        else:
            return 'Сейчас ночь'

a = SuperData(2024, 3, 1, 12)
print(a.get_season(2))
print(a.get_time_of_day(4))

