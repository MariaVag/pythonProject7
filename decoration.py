def is_prime(x):
    def wrapper(number):
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print('простое')
            else:
                print('составное')
        return wrapper


@is_prime
def sum_of_three(a, b, c):
    res = 4 + 6 + 8
    print(res)
