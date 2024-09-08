"""
URL: https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%AD%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0
Для нахождения всех простых чисел не больше заданного числа n, следуя методу Эратосфена, нужно выполнить следующие шаги:

1. Выписать подряд все целые числа от двух до n (2, 3, 4, …, n).
2. Пусть переменная p изначально равна двум — первому простому числу.
3. Зачеркнуть в списке числа от 2p до n, считая шагами по p (это будут числа, кратные p: 2p, 3p, 4p, …).
4. Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
5. Повторять шаги 3 и 4, пока возможно.
"""


def get_all_primes(n):

    if n < 2:
        return []

    numbers = [i for i in range(2, n + 1)]
    is_prime = [True] * len(numbers)

    for idx, num in enumerate(numbers):
        for i in range(2 * num - 2, len(numbers), num):
            is_prime[i] = False

    primes = [numbers[i] for i, num in enumerate(is_prime) if num]

    return primes


if __name__ == '__main__':
    primes = get_all_primes(100)
    print(primes)

