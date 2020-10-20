from random import randint as ran
<<<<<<< HEAD
=======

>>>>>>> Develop

def dados(numero):
    if numero >= 1 and numero <= 6:
        return True


def test_dados():
<<<<<<< HEAD
    a  = ran(0,6)
    assert dados(a)==True
=======
    a = ran(1, 6)
    assert dados(a) == True
>>>>>>> Develop
