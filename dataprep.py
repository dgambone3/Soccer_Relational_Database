import pandas as pd

# 1. Prepare GameTeam table
games = pd.read_csv('data/games.csv')
# get gameID, hometeamid, awayteamid, columns from games
cols = ['gameID', 'homeTeamID', 'awayTeamID']
gameteam = games[cols]
# 2. Add venueID to Team table, using teamID
teams = pd.read_csv('data/teams.csv')
venues = pd.read_csv('data/venue.csv')
teams = teams.merge(venues[['teamID','venueID']], on='teamID')
# reorder columns in teams to match schema.txt
cols = ['teamID', 'venueID', 'teamName']
teams = teams[cols]
# 3. Get venue ID into games from venues table, by joining on homeTeamID
games = games.merge(venues[['teamID', 'venueID']], left_on='homeTeamID', right_on='teamID')
games = games.drop('teamID', axis=1)
# 4. Get seasonID into games from seasons table, by joining on (leagueID,season)=(leagueID,year)
seasons = pd.read_csv('data/season.csv')
games = games.merge(seasons[['leagueID','year', 'seasonID']], left_on=['leagueID','season'], right_on=['leagueID','year'])
games = games.drop(['year', 'leagueID'], axis=1)
# 5. Rename date column in games to gameDate
games = games.rename(columns={'date': 'gameDate'})
# 6. Drop unnecessary game columns
cols = ['gameID', 'seasonID', 'venueID','gameDate', 'homeGoals', 'awayGoals']
games = games[cols]
# 7. Drop teamID from venue table
venues = venues.drop('teamID', axis=1)
# 8. Read in managerTeam table and cast dates to ISO datetime, drop managerName
managerteam = pd.read_csv('data/managerteam.csv')
managerteam['startDate'] = pd.to_datetime(managerteam['startDate'], format='%Y%m')
managerteam['endDate'] = pd.to_datetime(managerteam['endDate'], format='%Y%m', errors='coerce')
managerteam = managerteam.drop('managerName', axis=1)
# 9. Cast season startDate and endDate to ISO datetime, reorder columns to match schema.txt
seasons['startDate'] = pd.to_datetime(seasons['startDate'], format='%Y%m%d')
seasons['endDate'] = pd.to_datetime(seasons['endDate'], format='%Y%m%d')
cols = ['seasonID', 'leagueID', 'championID','year', 'startDate', 'endDate']
seasons = seasons[cols]
# 10. Read in appearances table, select necessary columns, rename shots column to numShots
appearances = pd.read_csv('data/appearances.csv')
cols = ['gameID', 'playerID', 'position', 'assists', 'shots', 'goals', 'yellowCard', 'redCard']
appearances = appearances[cols]
appearances = appearances.rename(columns={'shots': 'numShots', 'yellowCard': 'yellowCards', 'redCard': 'redCards'})
# 11. Read in Shot table, add row index as column shotID, select necessary columns, rename assisterID to assistID
shots = pd.read_csv('data/shots.csv')
shots['shotID'] = shots.index
cols = ['shotID', 'gameID', 'shooterID', 'assisterID', 'situation', 'shotType', 'shotResult']
shots = shots[cols]
shots = shots.rename(columns={'assisterID': 'assistID'})
# 12. Read in remaining tables, write all tables out to CSV files
players = pd.read_csv('data/players.csv', encoding_errors='replace')
managers = pd.read_csv('data/manager.csv')
leagues = pd.read_csv('data/leagues.csv')
leagues = leagues.rename(columns={'name': 'leagueName'})

tables = [gameteam, games, teams, venues, managerteam, seasons, appearances, shots, players, managers, leagues]
names = ['gameteam', 'game', 'team', 'venue', 'managerteam', 'season', 'appearance', 'shot', 'player', 'manager', 'league']
for table, name in zip(tables, names):
    table.to_csv('finalTables/{}.csv'.format(name), index=False)