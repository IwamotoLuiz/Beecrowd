def passo_1(texto):
    novo_texto = ''
    for char in texto:
        if char.isalpha():
            novo_texto += chr(ord(char) + 3)
        else:
            novo_texto += char

    return novo_texto


def passo_2(texto):
    texto_invertido = ''.join(reversed(texto))
    return texto_invertido


def passo_3(texto):
    meio = len(texto) // 2
    metade1 = texto[:meio]
    metade2 = texto[meio:]

    nova_metade2 = ''
    for char in metade2:
        nova_metade2 += chr(ord(char) - 1)

    novo_texto = metade1 + nova_metade2

    return novo_texto


# Leitura do número de casos de teste
N = int(input())
for i in range(N):
    M = str(input())
    print(passo_3(passo_2(passo_1(M))))

