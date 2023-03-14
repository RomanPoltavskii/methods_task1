# e^-x * sin * pi * x - th * x + 1 = 0, (0 <= x <= 3.5)

import math


def f(x):
    return math.e**(-x) * math.sin(math.pi * x) - math.tanh(x) + 1


def dichotomy(f, a, b, eps=1e-5):
    x = (a + b) / 2
    while abs(b - a) >= eps:
        x = (a + b) / 2
        if (f(x) * f(a)) <= 0:
            b = x
        else:
            a = x
    return x


x1 = dichotomy(f, 1, 1.5)
x2 = dichotomy(f, 1.8, 2)
x3 = dichotomy(f, 2.7, 3.5)
print('Первый корень ' + str(x1))
print(str(f(x1)) + '\n')
print('Второй корень ' + str(x2))
print(str(f(x2)) + '\n')
print('Третий корень ' + str(x3))
print(str(f(x3)) + '\n')

