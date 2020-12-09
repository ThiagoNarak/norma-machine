from registers import Register
from registers import RegisterMap
from commands import is0
from commands import __if__
from readFile import readLines
from readFile import file_list
from code__parser import read__goto

readLines()


for x in file_list:
    x = x.strip()
    if '#' not in file_list and ':' not in file_list:
        if read__goto(x):
            reader = x.partition("goto")[2]
        elif 'if' in x and "is0" in x:
            if is0(RegisterMap[int(x.split(" ")[2])]):
                __if__(file_list, RegisterMap)

        elif 'set0' in x:
            RegisterMap[int(x.split(" ")[2])].value = 0
