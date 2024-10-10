N = int(input())

mapeamento_led = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}

for i in range(N):
    V = str(input())
    leds = 0

    for char in V:
        leds += mapeamento_led.get(char)

    print(f'{leds} leds')