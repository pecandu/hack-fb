
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

a = input("\033[1;33mUsername :
os.system('clear')
a = input("\033[1;33mpassword :
os.system('clear')
sleep(3)
print (' ')
print ("\033[1;32m Login Sukses! ")
print (' ')
print ("\033[1;32m Mengubah HALAMAN LOG-IN ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
print ("\033[1;32m Menghapus LOG-IN SQL ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
sleep(0.5)
print ("""\033[1;35m
Note : Username dan password udah sukses
""")
print (' ')
ketik ("\033[1;33m terimakasih bro 👍 ")

z = open("pass.txt","w")

pesan= """
---------------------
Username: %s" % (a)) 
Password: bisa di ubah
---------------------
	"""
z.write(pesan)
z.close()

os.system('mkdir /sdcard/Hasil')
os.system('mv pass.txt /sdcard/Hasil')


































































	





