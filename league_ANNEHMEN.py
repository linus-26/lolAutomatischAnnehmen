import mouse
import time
import win32gui
import pyautogui

#0, 173, 150
#0 230 203

#7390 7400 7410

def get_pixel_colour(i_x, i_y):
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def funGo(posx, posy, ges, champ):
	print("Programm wird gestartet")
	while(1):
		pixel = get_pixel_colour(posx, posy)
		if((pixel[0] == 41) and (pixel[1] == 38) and (pixel[2] == 29)):
			print("ANNEHMEN, drücke in 5 Sekunden")
			for x in range(1, 3):
				print("Seks: " + str(x))
				time.sleep(1)

			mausx = str(mouse.get_position()[0])
			mausy = str(mouse.get_position()[1])

			mouse.move(posx - 477, posy - 138, absolute=True, duration=0.0)
			mouse.click('left')
			time.sleep(0.01)
			mouse.click('left')
			time.sleep(0.01)
			mouse.click('left')
			mouse.move(mausx, mausy, absolute=True, duration=0.0)

			print("Habe angenommen")

			pixel = get_pixel_colour(posx, posy)
			while((pixel[0] == 41) and (pixel[1] == 38) and (pixel[2] == 29)):
				print("Bereits angenommen")
				time.sleep(1)
				pixel = get_pixel_colour(posx, posy)

			time.sleep(0.5)
			pixel = get_pixel_colour(posx, posy)
			print("Pixel: " + str(pixel))
			if(((pixel[0] == 205) and (pixel[1] == 190) and (pixel[2] == 145)) or ((pixel[0] == 41) and (pixel[1] == 38) and (pixel[2] == 29))):
				print("Es haben nicht alle angenommen")
			else:
				print("In Champselect?")
				#Ist der Pixel vom neuen Chat da
				pixel = get_pixel_colour(posx, posy)
				if(((pixel[0] == 205) and (pixel[1] == 190) and (pixel[2] == 145)) or ((pixel[0] == 41) and (pixel[1] == 38) and (pixel[2] == 29))):
					print("Doch nicht in Champselect")
				else:
					print("Champselect")

					if(champ != ""):
						print("Warte 8 sek bis Pick")
						for x in range(1, 9):	
							print("Seks: " + str(x))
							time.sleep(1)

						print("\nklick auf Suchleiste")
						#klick auf Suchleiste
						mouse.move(posx - 314, posy - 601, absolute=True, duration=0.3)
						time.sleep(0.2)
						mouse.click('left')
						mouse.click('left')
						print("Suche nach " + champ)
						pyautogui.typewrite(champ)

						print("klick auf 1.Champ")
						#klick auf 1. Champ
						mouse.move(posx - 700, posy - 542, absolute=True, duration=0.3)
						time.sleep(0.2)
						mouse.click('left')
						mouse.click('left')

						print("Warte 16 sek bis Bann")
						for x in range(1, 17):
							print("Seks: " + str(x))
							time.sleep(1)
					else:
						print("Kein Champ angegeben. Banne in 25 Sekunden")
						for x in range(1, 26):
							print("Seks: " + str(x))
							time.sleep(1)

					
					
					print("\nklick auf Suchleiste")
					#klick auf Suchleiste
					mouse.move(posx - 314, posy - 601, absolute=True, duration=0.3)
					time.sleep(0.2)
					mouse.click('left')
					mouse.click('left')
					print("yasuo eingeben...")
					pyautogui.typewrite("yasuo")

					print("klick auf 1.Champ")
					#klick auf 1. Champ
					mouse.move(posx - 700, posy - 542, absolute=True, duration=0.3)
					time.sleep(0.2)
					mouse.click('left')
					mouse.click('left')

					print("klick auf Bannen\n")
					#klick auf Bann
					mouse.move(posx - 432, posy - 95, absolute=True, duration=0.3)
					time.sleep(0.2)
					mouse.click('left')
					mouse.click('left')
					print("Champ gebannt, beende Programm.")
					break



		elif((pixel[0] == 205) and (pixel[1] == 190) and (pixel[2] == 145)):
			print("Teste schon seit: " + str(ges + 1) + " Sekunden.")
			time.sleep(1)
			ges = ges + 1

		else:
			print("Schon im Game?")
			for x in range(1, 6):
				print("Seks: " + str(x))
				time.sleep(1)
			pixel = get_pixel_colour(posx, posy)
			if((pixel[0] == 205) and (pixel[1] == 190) and (pixel[2] == 145)):
				print("Doch noch nicht im Game 1")
			elif((pixel[0] == 41) and (pixel[1] == 38) and (pixel[2] == 29)):
				print("Doch noch nicht im Game 2")
			else:
				print("Nicht mehr in der Champselect. Beende Programm.")
				ges = 0
				break



def mainStart():
	print("\nGuten Hallo. Mit 'pos' wird die Position von League festgestellt.\nDabei bitte den Mauszeiger in die Mitte, auf das gelbe vom Chatsymbol setzen.\n\nAlle Befehle:\n- pos: Neue Position\n- go: Startet das Programm\n- wo: Setzt Mauszeiger auf die aktuelle Position\n")
	
	posx = 0
	posy = 0

	try:
		datei = open('leagueAnnehmen.txt', 'r')
		#print(datei.read())
		dateiInhalt = datei.read()
		getrennterDateiInhalt = dateiInhalt.split()
		print("Posx: " + getrennterDateiInhalt[0])
		print("Posy: " + getrennterDateiInhalt[1])
		posx = int(getrennterDateiInhalt[0])
		posy = int(getrennterDateiInhalt[1])
		datei.close()
	except(Exception):
		print("Position ist auf 0, 0.\n")
	
	
	ges = 0
	while(1):
		eingabe = input("\nEingabe:")
		print("\n")
		eingabeSplit = eingabe.split()
		eingabe1 = eingabeSplit[0]
		if(eingabe1 == "go"):
			champ = ""
			try:
				champ = eingabeSplit[1]
				print("Champ: " + champ)
			except(Exception):
				print("Kein Champ angegeben.")
			funGo(posx, posy, ges, champ)

		if(eingabe1 == "wo"):
			print("Setze Mauszeiger auf aktuelle Position.")
			mouse.move(posx, posy, absolute=True, duration=0.1)
			print("Posx: " + str(posx) + " Posy: " + str(posy))

		if(eingabe1 == "pos"):
			print("Position.")
			for x in range(1, 6):
				print(str(x))
				time.sleep(1)
			
			posx = mouse.get_position()[0]
			posy = mouse.get_position()[1]
			pixel = get_pixel_colour(posx, posy)
			print("Posx: " + str(posx) + " Posy: " + str(posy))

			print("Speicher Position")
			datei = open('leagueAnnehmen.txt', 'w')
			datei.write(str(posx) + " " + str(posy))
			datei.close()
			



mainStart()