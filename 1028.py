import math

# Leitura de casos de teste
N = int(input())

for i in range(N):
    # Leitura do número de figurinhas de cada um
    F1, F2 = map(int, input().split())

    # Determinação do tamanho das pilhas de figurinhas a partir do MDC
    pilhas = math.gcd(F1, F2)

    print(pilhas)