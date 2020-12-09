class Register:

    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def dec(register):
    register.value -= 1


def inc(register):
    register.value += 1


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


# Double all numbers using map and lambda

RegisterMap = dict()

for i in range(0, 64):
    RegisterMap[i] = Register("R{}".format(i), 0)
