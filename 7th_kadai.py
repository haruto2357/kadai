import numpy as np
import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
ans = (100 * a) + (10 * b) + c

num = int(input('Input number : '))
x = num // 100
y = (num % 100) // 10
z = num % 10
