import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill


    def run(self):
        evil = 100
        day = 0
        while evil > 0:
            if self.skill >= 30:
                evil -= 20
                day += 2
            elif self.skill <= 29:
                evil -= 10
                day += 5
            else:
                return
        print(f'{self.name} за {day} дней победил врагов')
        time.sleep(1)



knight1 = Knight(name='Lord Фаркуад', skill=20)
knight2 = Knight(name='Sir Шрек', skill=50)
print('Рыцари, вперед!')
knight1.start()
knight2.start()


knight1.join()
knight2.join()

print('Рыцари победили!')
