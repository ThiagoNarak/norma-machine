from registers import RegisterMap as dictMap


def is0(register):
    if register.value == 0:
        return True
    else:
        return False


def __if__(line, __dict__):
    control = 0
    while control == 0:
        for x in __dict__:
            if "inc" in line:
                dictMap[int(x.split(" ")[2])] += 1
            elif "dec" in line:
                dictMap[int(x.split(" ")[2])] -= 1
            elif "set0" in line:
                dictMap[int(x.split(" ")[2])] = 0
            elif "add" in line:
                dictMap[int(x.split(" ")[2])].value += dictMap[int(x.split(" ")[3])]
            elif "set" in line:
                dictMap[int(x.split(" ")[2])].value = dictMap[int(x.split(" ")[3])]
            elif "endif" in line:
                control = 1
