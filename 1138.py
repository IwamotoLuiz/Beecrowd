def contar_digitos_intervalo(A, B):
    def contar_ate_n(n):
        contagem = [0] * 10
        fator = 1
        while fator <= n:
            menor = n // (fator * 10)
            atual = (n // fator) % 10
            maior = n % fator

            # Contagem de 0 a 9 menos o atual dígito
            for i in range(10):
                contagem[i] += menor * fator

            # Contagem do dígito atual
            for i in range(atual):
                contagem[i] += fator

            contagem[atual] += maior + 1

            # Ajustar a contagem para o caso do dígito 0
            contagem[0] -= fator

            fator *= 10

        return contagem

    # Função que subtrai a contagem de 1 até A-1 da contagem de 1 até B
    contagem_total = contar_ate_n(B)
    if A > 1:
        contagem_ate_A_menos_1 = contar_ate_n(A - 1)
        for i in range(10):
            contagem_total[i] -= contagem_ate_A_menos_1[i]

    return contagem_total


# Leitura indefinida até encontrar "0 0"
while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    resultado = contar_digitos_intervalo(A, B)
    print(" ".join(map(str, resultado)))
