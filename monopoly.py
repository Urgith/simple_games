import matplotlib.pyplot as plt
import matplotlib
import random

def rysowanie_planszy():
  for i,pole in enumerate(pola):
    if i!=0 and i!=9 and i!=17 and i!=26:
      plt.gca().add_patch(matplotlib.patches.Rectangle((pole[0],pole[1]),1,1,color=pole[3]))
      plt.gca().add_patch(matplotlib.patches.Rectangle((pole[0],pole[1]),1,1,fill=False,color=pole[3]))
      if i==31:
        matplotlib.axes.Axes.text(plt.gca(),pole[0]+0.1,pole[1]+0.25,f'{pole[2]}$',fontsize=30,color='w')
      elif i==14:
        matplotlib.axes.Axes.text(plt.gca(),pole[0]-0.05,pole[1]+0.25,f'{pole[2]}$',fontsize=30,color='w')
      elif i==22:
        matplotlib.axes.Axes.text(plt.gca(),pole[0]+0.3,pole[1]+0.2,f'{pole[2]}',fontsize=30,color='w')
      else:
        matplotlib.axes.Axes.text(plt.gca(),pole[0]+0.01,pole[1]+0.01,f'{pole[2]}$',fontsize=10,color='w')
    else:
      plt.gca().add_patch(matplotlib.patches.Rectangle((pole[0],pole[1]),1,1,color=(0,0.2,1)))
      if i==0:
        matplotlib.axes.Axes.text(plt.gca(),pole[0],pole[1]+0.7,'Start',fontsize=10,color='w',rotation=-45)
      elif i==9:
        matplotlib.axes.Axes.text(plt.gca(),pole[0],pole[1]+0.7,'Areszt',fontsize=10,color='w',rotation=-45)
      elif i==17:
        matplotlib.axes.Axes.text(plt.gca(),pole[0],pole[1]+0.7,'Loteria',fontsize=10,color='w',rotation=-45)
      elif i==26:
        matplotlib.axes.Axes.text(plt.gca(),pole[0]-0.1,pole[1]+0.85,'Oszustwo',fontsize=10,color='w',rotation=-45)
  for gracz in gracze:
    plt.gca().add_patch(matplotlib.patches.Circle((gracz.x,gracz.y),0.1,color=gracz.color))
    for kupione in gracz.kupione:
      plt.gca().add_patch(matplotlib.patches.Rectangle((kupione[0]+0.03,kupione[1]+0.85-0.03),0.3,0.15,color=gracz.color))

def nowy_wykres(tura,cena):
  plt.close()
  plt.figure(figsize=(8,8))
  plt.axis('off')
  plt.xlim(0,10)
  plt.ylim(0,11)
  plt.gca().set_aspect('equal', adjustable='box')
  matplotlib.axes.Axes.text(plt.gca(),0.2,10.35,f'Money: {gracze[1].money}$',fontsize=15,color=gracze[1].color)
  matplotlib.axes.Axes.text(plt.gca(),0.2,0.35,f'Money: {gracze[0].money}$',fontsize=15,color=gracze[0].color)
  matplotlib.axes.Axes.text(plt.gca(),3.9,6.2,'Gracz',fontsize=30,color=gracze[tura%2].color)
  matplotlib.axes.Axes.text(plt.gca(),1.8,5.2,f'Naciśnij myszką aby kupić za {cena}$',fontsize=15,color=gracze[tura%2].color)
  matplotlib.axes.Axes.text(plt.gca(),1.4,4.2,'Kliknij dowolny przycisk aby nie kupić',fontsize=15,color=gracze[tura%2].color)


class Gra:

  def __init__(self,figure,tura):
    self.fig=figure
    self.tura=tura
    rysowanie_planszy()
    self.x=0
    self.y=0
    self.cid=self.fig.canvas.mpl_connect('button_press_event', self)
    self.dic=self.fig.canvas.mpl_connect('button_release_event', self)
    plt.axis('off')
    plt.xlim(0,10)
    plt.ylim(0,11)
    plt.gca().set_aspect('equal', adjustable='box')
    matplotlib.axes.Axes.text(plt.gca(),0.2,10.35,f'Money: {gracze[1].money}$',fontsize=15,color=gracze[1].color)
    matplotlib.axes.Axes.text(plt.gca(),0.2,0.35,f'Money: {gracze[0].money}$',fontsize=15,color=gracze[0].color)
    matplotlib.axes.Axes.text(plt.gca(),3.9,6.2,'Gracz',fontsize=30,color=gracze[tura%2].color)
    plt.show()

  def __call__(self, event):
    if self.dic:
      if event.inaxes:
        event.canvas.mpl_disconnect(self.cid)
        event.canvas.mpl_disconnect(self.dic)
    if event.inaxes:
      self.tura+=1
      self.x=event.x
      self.y=event.y
      Gracz.ruch(gracze[tura%2],tura,pola)
      plt.close()

class Gracz:

  def __init__(self,x,y,color):
    self.aktualne_pole=0
    self.xx=x
    self.yy=y
    self.x=pola[self.aktualne_pole][0]+self.xx
    self.y=pola[self.aktualne_pole][1]+self.yy
    self.color=color
    self.money=1000
    self.kupione=[]

  def ruch(self,tura,pola):
    self.aktualne_pole+=random.randint(1,6)+random.randint(1,6)
    if self.aktualne_pole>=34:
      self.aktualne_pole=self.aktualne_pole%34
      self.money+=200
    self.x=pola[self.aktualne_pole][0]+self.xx
    self.y=pola[self.aktualne_pole][1]+self.yy
    self.zakup(pola,tura)

  def zakup(self,pola,tura):
    if self.xx==0.15:
      if pola[self.aktualne_pole] in gracze[1].kupione:
        print('O nie!')
        self.money-=pola[self.aktualne_pole][2]//5
        gracze[1].money+=pola[self.aktualne_pole][2]//5
      elif pola[self.aktualne_pole] in gracze[0].kupione:
        print('To już jest moje')
      elif self.aktualne_pole==0 or self.aktualne_pole==9 or self.aktualne_pole==17 or self.aktualne_pole==26:
        pass
      elif self.aktualne_pole==31:
        self.money-=random.randint(10,150)
      elif self.aktualne_pole==14:
        self.money+=random.randint(10,150)
      elif self.aktualne_pole==22:
        self.money+=random.randint(-150,150)
      else:
        if self.money>=pola[self.aktualne_pole][2]:
          nowy_wykres(tura,pola[self.aktualne_pole][2])
          rysowanie_planszy()

          zakupiono=plt.waitforbuttonpress()
          if not zakupiono:
            print('Kupuję!')
            self.kupione.append(pola[self.aktualne_pole])
            self.money-=pola[self.aktualne_pole][2]

    else:
      if pola[self.aktualne_pole] in gracze[0].kupione:
        print('O nie!')
        self.money-=pola[self.aktualne_pole][2]//5
        gracze[0].money+=pola[self.aktualne_pole][2]//5
      elif pola[self.aktualne_pole] in gracze[1].kupione:
        print('To już jest moje')
      elif self.aktualne_pole==0 or self.aktualne_pole==9 or self.aktualne_pole==17 or self.aktualne_pole==26:
        pass
      elif self.aktualne_pole==31:
        self.money-=random.randint(10,150)
      elif self.aktualne_pole==14:
        self.money+=random.randint(10,150)
      elif self.aktualne_pole==22:
        self.money+=random.randint(-150,150)
      else:
        if self.money>=pola[self.aktualne_pole][2]:
          nowy_wykres(tura,pola[self.aktualne_pole][2])
          rysowanie_planszy()

          zakupiono=plt.waitforbuttonpress()
          if not zakupiono:
            print('Kupuję!')
            self.kupione.append(pola[self.aktualne_pole])
            self.money-=pola[self.aktualne_pole][2]


pola=((0,1),(1,1,30,(0,255/255,255/255)),(2,1,35,(0,255/255,255/255)),(3,1,40,(0,255/255,255/255)),(4,1,50,(0,255/255,255/255)),(5,1,150,(128/255,128/255,128/255)),(6,1,60,(30/255,144/255,255/255)),(7,1,65,(30/255,144/255,255/255)),(8,1,70,(30/255,144/255,255/255)),(9,1),(9,2,90,(0,255/255,0)),(9,3,100,(0,255/255,0)),(9,4,110,(0,255/255,0)),(9,5,150,(128/255,128/255,128/255)),(9,6,'+','g'),(9,7,125,(173/255,255/255,47/255)),(9,8,135,(173/255,255/255,47/255)),(9,9),(8,9,160,(255/255,215/255,0)),(7,9,175,(255/255,215/255,0)),(6,9,190,(255/255,215/255,0)),(5,9,150,(128/255,128/255,128/255)),(4,9,'?',(128/255,128/255,128/255)),(3,9,210,(255/255,140/255,0)),(2,9,225,(255/255,140/255,0)),(1,9,240,(255/255,140/255,0)),(0,9),(0,8,270,(255/255,20/255,147/255)),(0,7,290,(255/255,20/255,147/255)),(0,6,310,(255/255,20/255,147/255)),(0,5,150,(128/255,128/255,128/255)),(0,4,'-',(255/255,0,0)),(0,3,350,(165/255,42/255,42/255)),(0,2,400,(165/255,42/255,42/255)))
tura=0
gracze=(Gracz(0.15,0.35,'k'),Gracz(0.85,0.35,(0.5,0,1)))

while gracze[0].money>=0 and gracze[1].money>=0:
  fig=plt.figure(figsize=(8,8))
  klikniecie=Gra(fig,tura)
  tura=klikniecie.tura
