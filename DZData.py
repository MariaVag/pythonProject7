from datetime import datetime


class SuperDate(datetime):
    season = {(12, 1, 2): 'Зима', range(3, 6): 'Весна', range(6, 10): 'Лето', range(10, 12): 'Осень'}
    times = {range(6, 12): 'Доброе утро!', range(12, 18): 'Добрый день!', range(18, 24): 'Добрый вечер!', range(0, 6): 'Доброй ночи!'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)

    def get_season(self):
        for current in self.season:
            if self.date.month in current:
                return self.season[current]

    def get_time_of_day(self):
        for current in self.times:
            if self.date.hour in current:
                return self.times[current]



a = SuperDate(2024, 4, 22, 4)

print(a.get_season)
print(a.get_time_of_day)

