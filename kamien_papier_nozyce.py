import matplotlib.pyplot as plt
import matplotlib
import random
import time
fig, ax = plt.subplots()

plt.xlabel('Papier                     Kamień                      Nożyce')
plt.xticks((0,1,1))
plt.xticks((1,2,1))
plt.xlim(0,3)
plt.ylim(0,1)
plt.yticks((0,1,1))
plt.grid(color='black')

def onclick(event):
		
		print('button=%d, x=%d, y=%d'%(event.button,
			   event.x,event.y))
		a = event.x
		b = event.y
		print(a,b)
		
		if a>81 and a<242 and b>57 and b<418:
			fig, ax = plt.subplots()


			plt.xticks((0,1,1))
			plt.xticks((1,2,1))
			plt.xlim(0,3)
			plt.ylim(0,1)
			plt.yticks((0,1,1))
			plt.grid(color='black')
			t = random.choice(['Wygrałeś! :)','Przegrałeś :(','Remis'])
			if t == 'Wygrałeś! :)':
				ax.set_title('Komputer: kamień ' +t)
			elif t == 'Przegrałeś :(':
				ax.set_title('Komputer: nożyce ' +t)
			elif t == 'Remis':
				ax.set_title('Komputer: papier ' +t)
			plt.show()
			
		if a>242 and a<409 and b>57 and b<418:
			fig, ax = plt.subplots()

			
			plt.xticks((0,1,1))
			plt.xticks((1,2,1))
			plt.xlim(0,3)
			plt.ylim(0,1)
			plt.yticks((0,1,1))
			plt.grid(color='black')
			t = random.choice(['Wygrałeś! :)','Przegrałeś :(','Remis'])
			if t == 'Wygrałeś! :)':
				ax.set_title('Komputer: nożyce ' +t)
			elif t == 'Przegrałeś :(':
				ax.set_title('Komputer: papier ' +t)
			elif t == 'Remis':
				ax.set_title('Komputer: kamień ' +t)
			plt.show()
			
		if a>409 and a<574 and b>57 and b<418:
			fig, ax = plt.subplots()


			plt.xticks((0,1,1))
			plt.xticks((1,2,1))
			plt.xlim(0,3)
			plt.ylim(0,1)
			plt.yticks((0,1,1))
			plt.grid(color='black')
			t = random.choice(['Wygrałeś! :)','Przegrałeś :(','Remis'])
			if t == 'Wygrałeś! :)':
				ax.set_title('Komputer: papier ' +t)
			elif t == 'Przegrałeś :(':
				ax.set_title('Komputer: kamień ' +t)
			elif t == 'Remis':
				ax.set_title('Komputer: nożyce ' +t)
			plt.show()
			
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
