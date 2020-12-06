from registers import Register
from commands import dec
from commands import inc
from commands import is0
from commands import goto
from commands import set0
from commands import setRiRj
from commands import add
from readFile import file_list
import re

r0 = Register()
r0.name = "R0"
r1 = Register()
r1.name = "R1"
r2 = Register()
r2.name = "R2"
r3 = Register()
r3.name = "R3"
r4 = Register()
r4.name = "R4"
r5 = Register()
r5.name = "R5"
r6 = Register()
r6.name = "R6"
r7 = Register()
r7.name = "R7"
r8 = Register()
r8.name = "R8"
r9 = Register()
r9.name = "R9"
r10 = Register()
r10.name = "R10"
r11 = Register()
r11.name = "R11"
r12 = Register()
r12.name = "R12"
r13 = Register()
r13.name = "R13"
r14 = Register()
r14.name = "R14"
r15 = Register()
r15.name = "R15"
r16 = Register()
r16.name = "R16"
r17 = Register()
r17.name = "R17"
r18 = Register()
r18.name = "R18"
r19 = Register()
r19.name = "R19"
r20 = Register()
r20.name = "R20"
r21 = Register()
r21.name = "R21"
r22 = Register()
r22.name = "R22"
r23 = Register()
r23.name = "R23"
r24 = Register()
r24.name = "R24"
r25 = Register()
r25.name = "R25"
r26 = Register()
r26.name = "R26"
r27 = Register()
r27.name = "R27"
r28 = Register()
r28.name = "R28"
r29 = Register()
r29.name = "R29"
r30 = Register()
r30.name = "R30"
r31 = Register()
r31.name = "R31"
r32 = Register()
r32.name = "R32"
r33 = Register()
r33.name = "R33"
r34 = Register()
r34.name = "R34"
r35 = Register()
r35.name = "R35"
r36 = Register()
r36.name = "R36"
r37 = Register()
r37.name = "R37"
r38 = Register()
r38.name = "R38"
r39 = Register()
r39.name = "R39"
r40 = Register()
r40.name = "R40"
r41 = Register()
r41.name = "R41"
r42 = Register()
r42.name = "R42"
r43 = Register()
r43.name = "R43"
r44 = Register()
r44.name = "R44"
r45 = Register()
r45.name = "R45"
r46 = Register()
r46.name = "R46"
r47 = Register()
r47.name = "R47"
r48 = Register()
r48.name = "R48"
r49 = Register()
r49.name = "R49"
r50 = Register()
r50.name = "R50"
r51 = Register()
r51.name = "R51"
r52 = Register()
r52.name = "R52"
r53 = Register()
r53.name = "R53"
r54 = Register()
r54.name = "R54"
r55 = Register()
r55.name = "R55"
r56 = Register()
r56.name = "R56"
r57 = Register()
r57.name = "R57"
r58 = Register()
r58.name = "R58"
r59 = Register()
r59.name = "R59"
r60 = Register()
r60.name = "R60"
r61 = Register()
r61.name = "R61"
r62 = Register()
r62.name = "R62"
r63 = Register()
r63.name = "R63"

print(r0.value)
print(is0(0, r0))
inc(r1)
print("r1", r1.value)
r0 = inc(r0)
print(r0.value)

