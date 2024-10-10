try:
    while True:
        v, t = map(int, input().split())
        resultado = (v*2) * t

        print(resultado)
except EOFError:
    pass
