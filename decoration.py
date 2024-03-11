def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res % 2 == 0:
            ent = 'Простое'
        else:
            ent = 'Составное'

            print(ent)
            return res
    return wrapper


@is_prime
def sum_of_three(a, b, c):
    return a + b + c


result = sum_of_three(54, 23, 12)
print(result)
