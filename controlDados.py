from random import randint as ran


def retornarTiros(cantidad):
    tiros = []
    for i in range(cantidad):
        print(i)
        tiros.append(ran(1, 6))
    return tiros
