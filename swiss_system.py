from collections import defaultdict
import pandas as pd
import ast


class Team:

    def __init__(self, name, wins=0, loses=0, opponents=[]):
        self.name = name
        self.wins = wins
        self.loses = loses
        self.opponents = opponents

        self.points = 0

    def __str__(self):
        return f'W:{self.wins}'.ljust(5) + f'L:{self.loses}'.ljust(6) + f'P:{self.points}'.ljust(7) + str(self.opponents)


class SwissSystem:

    def __init__(self, names=None):
        self.teams = {}
        self.games = []

        if names is not None:
            self.create_tournament(names)

    def create_tournament(self, names):
        for name in names:
            self.teams[name] = Team(name)

        self.max_name_len = max(map(lambda x: len(x), self.teams.keys()))

    def add_teams(self, teams):
        for team in teams:
            self.teams[team.name] = team

        self.max_name_len = max(map(lambda x: len(x), self.teams.keys()))
        self.calculate_points()

    def add_game(self, team1, team2, win, load):
        self.games.append((team1, team2, win))
        if load:
            return

        self.teams[team1].opponents.append(team2)
        self.teams[team2].opponents.append(team1)

        if win:
            self.teams[team1].wins += 1
            self.teams[team2].loses += 1

            for team in self.teams[team1].opponents:
                self.teams[team].points += 1
            for team in self.teams[team2].opponents:
                self.teams[team].points -= 1
        else:
            self.teams[team2].wins += 1
            self.teams[team1].loses += 1

            for team in self.teams[team2].opponents:
                self.teams[team].points += 1
            for team in self.teams[team1].opponents:
                self.teams[team].points -= 1

    def add_games(self, games, load=False):
        for game in games:
            self.add_game(*game, load)

    def calculate_points(self):
        for team in self.teams.values():
            points = 0

            for opponent in team.opponents:
                points += (self.teams[opponent].wins - self.teams[opponent].loses)

            team.points = points

    def get_same_wins(self):
        groups = defaultdict(list)

        for team in self.teams.values():
            groups[team.wins].append((team.name, team.points))

        return groups

    def save(self):
        df = pd.DataFrame(self.games, columns=['Team1', 'Team2', 'Team1_won'])

        to_save = []
        for team in sorted(self.teams.values(), key=lambda v: (v.wins, -v.loses, v.points), reverse=True):
            to_save.append([team.name, team.wins, team.loses, team.points, team.opponents])

        df2 = pd.DataFrame(to_save, columns=['Team', 'Wins', 'Losses', 'Points', 'Faced_Opponents'])

        writer = pd.ExcelWriter('swiss_system.xlsx', engine='xlsxwriter')
        df2.to_excel(writer, sheet_name='standing', index=False)
        df.to_excel(writer, sheet_name='games', index=False)

        writer.save()

    @staticmethod
    def load(file):
        dfs = pd.read_excel(file, sheet_name=None)

        new_teams = []
        teams = []
        games = []
        for _, game in dfs['standing'].iterrows():
            new_teams.append(Team(game[0], int(game[1]), int(game[2]), ast.literal_eval(game[4])))
            teams.append(game[0])
        for _, game in dfs['games'].iterrows():
            games.append((game[0], game[1], game[2]))

        tournament = SwissSystem(teams)
        tournament.add_games(games, load=True)
        tournament.add_teams(new_teams)

        return tournament

    def __str__(self):
        representation = ''
        for name, team in sorted(self.teams.items(), key=lambda kv: (kv[1].wins, -kv[1].loses, kv[1].points), reverse=True):
            representation += name.ljust(self.max_name_len + 2) + str(team) + '\n'

        return representation

# ---------- FROM 3RD ROUND OF SECOND STAGE ---------- #
system = SwissSystem()

teams = (
    Team('Natus Vincere', 2, 0, ['G2 Esports', 'BIG']),
    Team('Team Spirit', 2, 0, ['FURIA Esports', 'Heroic']),
    Team('Copenhages Flames', 2, 0, ['Bad News Eagles', 'ENCE']),
    Team('Ninjas in Pyjamas', 2, 0, ['Team Vitality', 'Cloud9']),
    Team('Cloud9', 1, 1, ['Outsiders', 'Ninjas in Pyjamas']),
    Team('ENCE', 1, 1, ['FaZe Clan', 'Copenhages Flames']),
    Team('Heroic', 1, 1, ['Team Liquid', 'Team Spirit']),
    Team('BIG', 1, 1, ['Imperial Esports', 'Natus Vincere']),
    Team('FURIA Esports', 1, 1, ['Team Spirit', 'Team Liquid']),
    Team('G2 Esports', 1, 1, ['Natus Vincere', 'Imperial Esports']),
    Team('FaZe Clan', 1, 1, ['ENCE', 'Bad News Eagles']),
    Team('Outsiders', 1, 1, ['Cloud9', 'Team Vitality']),
    Team('Team Vitality', 0, 2, ['Ninjas in Pyjamas', 'Outsiders']),
    Team('Bad News Eagles', 0, 2, ['Copenhages Flames', 'FaZe Clan']),
    Team('Imperial Esports', 0, 2, ['BIG', 'G2 Esports']),
    Team('Team Liquid', 0, 2, ['Heroic', 'FURIA Esports'])
)
system.add_teams(teams)

new_games = (
    ('Heroic', 'G2 Esports', True),
    ('ENCE', 'Outsiders', True),
    ('Cloud9', 'FaZe Clan', False),
    ('BIG', 'FURIA Esports', False),
    ('Team Spirit', 'Copenhages Flames', True),
    ('Natus Vincere', 'Ninjas in Pyjamas', True),
    ('Team Vitality', 'Team Liquid', True),
    ('Bad News Eagles', 'Imperial Esports', False)
)
system.add_games(new_games)

system.save()

print(system)

# ---------- FROM THE BEGINNING ---------- #
teams = (
    'ENCE', 'G2 Esports', 'forZe', 'Astralis', 'Team Vitality', 'MIBR',
    'Imperial Esports', 'Bad News Eagles', 'Eternal Fire', 'Team Spirit',
    'Outsiders', 'Complexity Gaming', 'IHC Esports', 'Renegades',
    'Team Liquid', '9z Team'
)
tournament = SwissSystem(teams)

new_games = ()
tournament.add_games(new_games)

print(tournament)

# ---------- 2ND STAGE ---------- #
teams = (
    'Heroic', 'Copenhages Flames', 'BIG', 'Cloud9','FURIA Esports',
    'FaZe Clan', 'Ninjas in Pyjamas', 'Natus Vincere', 'G2 Esports',
    'Team Vitality', 'ENCE', 'Team Spirit', 'Outsiders', 'Imperial Esports',
    'Bad News Eagles', 'Team Liquid'
)
tournament = SwissSystem(teams)

new_games = ()
tournament.add_games(new_games)

print(tournament)

# ---------- LOAD ---------- #
loaded = SwissSystem.load('swiss_system.xlsx')

print(loaded)
