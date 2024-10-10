import math
from math import factorial

try:
    while True:
        M, N = map(int, input().split())
        resultado = factorial(M) + factorial(N)

        print(resultado)
except EOFError:
    pass
