from math import hypot

try:
    while True:
        D, VF, VG = map(int, input().split())

        # Calcula a distância a ser percorrida pelos guardas
        hipotenusa = hypot(12, D)

        d_vf = 12/VF
        d_vg = hipotenusa/VG

        if d_vg <= d_vf:
            print('S')
        else:
            print('N')
except EOFError:
    pass
