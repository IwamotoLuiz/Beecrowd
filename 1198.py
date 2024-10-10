try:
    while True:
        aliados, inimigos = map(int, input().split())
        resultado = abs(aliados - inimigos)

        print(resultado)
except EOFError:
    pass
