# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументоd

def get_my_func(n):
    if n <= 2:
        def my_func(x):
            return x + 2
    elif n == 23:
        def my_func(x):
            return x *3
    else:
        raise Exception('I get')
    return my_func

my_num = [1, 2, 3, 23, 45, 87]

funci_1 = get_my_func(n=2)
finci_2 = get_my_func(n=23)
result = map(funci_1, my_num)
print(list(result))
result = map(finci_2, my_num)
print(list(result))



# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию
# с использованием def. Например, возведение числа в квадрат

numis = lambda x: x**2
resultates = numis(67)
print(resultates)

def numbers(x):
    return x ** 2
print (numbers(5678))


# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

class Rect:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a * b
pogr = Rect(8)
print(pogr(4))
