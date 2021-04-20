# 10 numeri casuali tra 1 e 50

import random           #importa modulo
from math import sqrt   #importa solo una funzione dal modulo
from math import *      #importa modulo

for numero in range(10):
    valore = random.randint(1, 50)
    print(valore)
