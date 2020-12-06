def dec(register):
    register.value -= 1


def inc(register):
    register.value += 1


def is0(value, register):
    if register.value == value:
        return True
    else:
        return False


def goto(line__name, list):
    for x in list:
        if line__name in x:
            return x
    return "TAG NÃO ENCONTRADA"


def set0(value, register):
    register.value = value


def setRiRj(register__i, register__j):
    register__i.value = register__j.value


def add(register__i, register__j):
    register__i.value += register__j.value

