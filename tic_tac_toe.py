import pygame


def quit():
    import sys

    pygame.quit()
    sys.exit(0)


class Game():

    def __init__(self, screen_size, size, win):
        self.game_screen = pygame.display.set_mode((screen_size, screen_size))

        self.full_field_size = screen_size / size
        self.field_size = int(self.full_field_size*24 / 25)

        self.positions = [-1 for i in range(size**2)]
        self.fields = []

        self.turn = 1
        self.size = size
        self.win = win

        self.creating_fields(size, screen_size)
        self.drawing_fields()
        self.creating_wins()

    def creating_fields(self, size, screen):
        for i in range(size**2):
            self.fields.append(pygame.Rect(int(i * self.full_field_size) % screen, self.full_field_size * ((i*self.full_field_size) // screen), self.field_size, self.field_size))

    def drawing_fields(self):
        for field in self.fields:
            pygame.draw.rect(self.game_screen, (255, 255, 255), field)

    def drawing_circles_and_crosses(self):
        for i, position in enumerate(self.positions):
            if position == 1:
                pygame.draw.circle(self.game_screen, (0, 0, 0), (self.fields[i].x + (self.field_size // 2), self.fields[i].y + (self.field_size // 2)), self.field_size // 3, int(self.full_field_size / 30) + 1)

            elif position == 0:
                pygame.draw.line(self.game_screen, (0, 0, 0), (self.fields[i].x + (self.field_size // 8), self.fields[i].y + (self.field_size // 8)), (self.fields[i].x + (self.field_size*7) // 8, self.fields[i].y + (self.field_size*7) // 8), int(self.full_field_size / 30) + 1)
                pygame.draw.line(self.game_screen, (0, 0, 0), (self.fields[i].x + (self.field_size // 8), self.fields[i].y + (self.field_size*7) // 8), (self.fields[i].x + (self.field_size*7) // 8, self.fields[i].y + (self.field_size // 8)), int(self.full_field_size / 30) + 1)

    def creating_wins(self):
        self.wins = {}
        rows = []

        for i in range(self.size):
            for j in range(self.size - self.win + 1):
                row = list(range((self.size*i) + j, (self.size*i) + self.win + j))
                rows.append(row)

        for i in range(self.size):
            for j in range(self.size - self.win + 1):
                row = list(range((self.size*j) + i, (self.size*j) + (self.size * self.win), self.size))
                rows.append(row)

        for i in range(2*(self.size - self.win) + 1):
            multiplier = self.size - self.win + 1 - abs(i - (self.size - self.win))

            for j in range(multiplier):
               row = list(range(self.function1(i) + j*(self.size + 1), self.function1(i) + (self.win + j - 1)*(self.size + 1) + 1, self.size + 1))
               rows.append(row)

        for i in range(2*(self.size - self.win) + 1):
            multiplier = self.size - self.win + 1 - abs(i - (self.size - self.win))

            for j in range(multiplier):
               row = list(range(self.function2(i) - j*(self.size - 1), self.function2(i) - (self.win + j - 1)*(self.size - 1) - 1, 1 - self.size))
               rows.append(row)

        for i in range(self.size**2):
            for row in rows:
                if i in row:
                    if i in self.wins:
                        self.wins[i].append(row)
                    else:
                        self.wins[i] = [row]

    def function1(self, n):
        max = (2*(self.size - self.win) + 1) // 2

        if n <= max:
            return self.size * (max - n)
        else:
            return n - max

    def function2(self, n):
        max = (2*(self.size - self.win) + 1) // 2

        if n <= max:
            return 2*sum(range(self.size)) - (self.size * (max - n))
        else:
            return 2*sum(range(self.size)) + n - max

    def checking_win(self, check):
        for win in self.wins[check]:
            counter = 0

            for pos in win:
                if self.positions[pos] == 0:
                    counter += 1

            if counter == len(win):
                return 'Cross won'

        for win in self.wins[check]:
            counter = 0

            for pos in win:
                if self.positions[pos] == 1:
                    counter += 1

            if counter == len(win):
                return 'Circle won'


game = Game(800, 3, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button==1:
            mouse_position = pygame.mouse.get_pos()

            for i, field in enumerate(game.fields):
                if field.collidepoint(mouse_position) and game.positions[i] == -1:
                    game.positions[i] = game.turn % 2
                    game.drawing_circles_and_crosses()
                    game.turn += 1

                    check = game.checking_win(i)
                    if check:
                        print(check)
                        game = Game(800, 3, 3)

                    if not -1 in game.positions:
                        print('Draw')
                        game = Game(800, 3, 3)

        elif event.type == pygame.QUIT:
            quit()

    pygame.display.flip()
