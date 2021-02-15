import pygame


pygame.display.set_mode()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
PINK = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

colours = {
  0:pygame.image.load('dane/poziomo.jpg').convert(),
  10:pygame.image.load('dane/pionowo.jpg').convert(),

  3:pygame.image.load('dane/czarny.jpg').convert(),

  5:pygame.image.load('dane/lg.jpg').convert(),
  50:pygame.image.load('dane/ld.jpg').convert(),

  6:pygame.image.load('dane/pg.jpg').convert(),
  60:pygame.image.load('dane/pd.jpg').convert(),

  7:pygame.image.load('dane/pd.jpg').convert(),
  70:pygame.image.load('dane/ld.jpg').convert(),

  8:pygame.image.load('dane/pg.jpg').convert(),
  80:pygame.image.load('dane/lg.jpg').convert()
}

trawa = pygame.image.load('dane/trawa.jpg').convert()
zacznij = pygame.image.load('dane/zacznij.jpg').convert()
domek = pygame.image.load('dane/domek.jpg').convert()
glosnik = pygame.image.load('dane/glosnik.jpg').convert()
glosnik_wylaczony = pygame.image.load('dane/glosnik_wylaczony.jpg').convert()

mysz = pygame.image.load('dane/mysz.jpg').convert()
szczur = pygame.image.load('dane/szczur.jpg').convert()

celownik_zielony = pygame.image.load('dane/celownik_zielony.jpg').convert()
celownik_zolty = pygame.image.load('dane/celownik_zolty.jpg').convert()
celownik_niebieski = pygame.image.load('dane/celownik_niebieski.jpg').convert()
celownik_rozowy = pygame.image.load('dane/celownik_rozowy.jpg').convert()
zasieg_zielony = pygame.image.load('dane/zasieg_zielony.jpg').convert()
zasieg_zolty = pygame.image.load('dane/zasieg_zolty.jpg').convert()
zasieg_niebieski = pygame.image.load('dane/zasieg_niebieski.jpg').convert()
zasieg_rozowy = pygame.image.load('dane/zasieg_rozowy.jpg').convert()
dolar_zielony = pygame.image.load('dane/dolar_zielony.jpg').convert()
dolar_zolty = pygame.image.load('dane/dolar_zolty.jpg').convert()
dolar_niebieski = pygame.image.load('dane/dolar_niebieski.jpg').convert()
dolar_rozowy = pygame.image.load('dane/dolar_rozowy.jpg').convert()
atak_zielony = pygame.image.load('dane/atak_zielony.jpg').convert()
atak_zolty = pygame.image.load('dane/atak_zolty.jpg').convert()
atak_niebieski = pygame.image.load('dane/atak_niebieski.jpg').convert()
atak_rozowy = pygame.image.load('dane/atak_rozowy.jpg').convert()

map = (
  ( 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
  (10, 1, 1, 1, 1, 1, 1, 5, 0, 0, 8, 1, 1, 1, 5, 0, 8, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 0, 8, 1, 1, 1, 1, 1, 1),
  (50, 0, 0, 8, 1, 1, 1,10, 1, 1,10, 1, 1, 5, 7, 1,10, 1, 1, 5, 0, 0, 0, 0, 0, 7, 1, 1,10, 1,80, 0, 0, 6, 1),
  ( 1, 1, 1,10, 1, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1, 1,10, 1),
  ( 1, 5, 0,10, 0, 0, 0,10, 0, 0,10, 0, 0,10, 0, 0,10, 0, 0,10, 0, 0, 0, 0, 0, 8, 1, 1,10, 1,10, 1, 1,10, 1),
  ( 1,10, 1,10, 1, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1, 1, 1, 1,10, 1, 1,50, 0, 0, 0, 0, 7, 1),
  ( 1,70, 0,10, 0, 0, 0,10, 0, 0,10, 0, 0,10, 0, 0,10, 0, 0,10, 0, 6, 1, 1, 1,10, 1, 1, 1, 1,10, 1, 1, 1, 1),
  ( 1, 1, 1,10, 1, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1,10, 1, 5, 0,10, 0, 8, 1, 1,10, 1, 1, 1, 1),
  ( 1, 1, 1,10, 1, 1, 5, 7, 1, 1,10, 1, 1,10, 1, 1,10, 1, 1,10, 1,10, 1,10, 1,10, 1,10, 1, 1,10, 1, 1, 1, 1),
  ( 1, 1, 1,10, 1, 1,10, 1, 1, 1,10, 1, 1,10, 1, 1,50, 0, 0, 7, 1,10, 1,10, 1,10, 1,10, 1, 1,50, 8, 1, 1, 1),
  ( 1, 1, 1,10, 1, 1,70, 6, 1, 1,50, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1,10, 1,70, 0,60, 1,10, 1, 1, 1,10, 1, 1, 1),
  ( 1, 1, 1,10, 1, 1, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1, 1, 1, 1, 1,10, 1, 1, 1,10, 1, 1, 1),
  ( 1, 1, 1,10, 1,80, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 0, 6, 1),
  ( 1, 1, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1, 1, 1, 1, 1,10, 1, 1, 1,10, 1,10, 1),
  ( 1, 1, 1,10, 1,50, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1,10, 1, 5, 0,10, 0, 7, 1),
  ( 1, 1, 1,10, 1, 1, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1,10, 1, 1, 1),
  ( 1,80, 0,60, 1, 1, 1,70, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1,10, 1, 1, 1),
  ( 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1,10, 1, 1, 1),
  ( 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 8, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1,50, 0, 8, 1),
  ( 1,50, 8, 1, 1, 5, 0, 0, 0, 8, 1, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,10, 1, 1, 1,10, 1),
  ( 1, 1,10, 1, 1,10, 1, 1, 1,10, 1, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10, 1,70, 6, 1, 1,10, 1),
  ( 1, 1,50, 8, 1,10, 1, 1, 1,10, 1, 1,10, 1,10, 1,10, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1,10, 1, 1,10, 1, 1,10, 1),
  ( 1, 1, 1,10, 1,10, 1, 1, 1,50, 0, 0, 7, 1,10, 1,10, 1, 3, 3, 3, 0, 0, 0, 0, 0, 0,60, 1, 1,70, 0, 0,60, 1),
  ( 1, 1, 1,50, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1,50, 0, 7, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
  ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

enemies = {
  GRAY:(1, 5, 1, 1, 15),
  BLACK:(0.8, 8, 2, 3, 17),
  WHITE:(1.2, 12, 2, 2, 20)
}

waves = (
  ((100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY), (100,GRAY)),
  ((110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY), (110,GRAY)),
  ((121,GRAY), (121,GRAY), (121,GRAY), (121,GRAY), (121,GRAY), (200,BLACK), (200,BLACK), (200,BLACK), (200,BLACK), (200,BLACK)),
  ((133.1,GRAY), (133.1,GRAY), (133.1,GRAY), (133.1,GRAY), (133.1,GRAY), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK), (220,BLACK)),
  ((146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (146.41,GRAY), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK), (242,BLACK)),
  ((161.051,GRAY), (161.051,GRAY), (161.051,GRAY), (161.051,GRAY), (161.051,GRAY), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (266.2,BLACK), (250,WHITE), (250,WHITE), (250,WHITE), (250,WHITE), (250,WHITE))
)

TILESIZE = 25
MAPWIDTH = len(map[0])
MAPHEIGHT = len(map)

GAME_WIDTH = TILESIZE*MAPWIDTH + 100
GAME_HEIGHT = TILESIZE*MAPHEIGHT + 100

LISTA_WIEZ = (
  ((GAME_WIDTH - 90, 20, 40, 40), GREEN, pygame.Rect(GAME_WIDTH - 90, 20, 40, 40)),
  ((GAME_WIDTH - 90, 80, 40, 40), YELLOW, pygame.Rect(GAME_WIDTH - 90, 80, 40, 40)),
  ((GAME_WIDTH - 90, 140, 40, 40), BLUE, pygame.Rect(GAME_WIDTH - 90, 140, 40, 40)),
  ((GAME_WIDTH - 90, 200, 40, 40), PINK, pygame.Rect(GAME_WIDTH - 90, 200, 40, 40))
)
