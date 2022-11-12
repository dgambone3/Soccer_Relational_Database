import pandas as pd

# 0. convert csvs to pd dataframes
games = pd.read_csv('data/games.csv')
teams = pd.read_csv('data/teams.csv')
venues = pd.read_csv('data/venue.csv')
seasons = pd.read_csv('data/season.csv')
managerteam = pd.read_csv('data/managerteam.csv')
appearances = pd.read_csv('data/appearances.csv')
shots = pd.read_csv('data/shots.csv')
players = pd.read_csv('data/players.csv')
managers = pd.read_csv('data/manager.csv')
leagues = pd.read_csv('data/leagues.csv')

# =========== Data Processing ====================================

# 1. Prepare GameTeam table
# get gameID, hometeamid, awayteamid, columns from games
cols = ['gameID', 'homeTeamID', 'awayTeamID']
gameteam = games[cols]

# 2. Add venueID to Team table, using teamID
teams = teams.merge(venues[['teamID','venueID']], on='teamID')
# reorder columns in teams to match schema.txt
cols = ['teamID', 'venueID', 'teamName']
teams = teams[cols]

# 3. Get venue ID into games from venues table, by joining on homeTeamID
games = games.merge(venues[['teamID', 'venueID']], left_on='homeTeamID', right_on='teamID')
games = games.drop('teamID', axis=1)

# 4. Get seasonID into games from seasons table, by joining on (leagueID,season)=(leagueID,year)
games = games.merge(seasons[['leagueID','year', 'seasonID']], left_on=['leagueID','season'], right_on=['leagueID','year'])
games = games.drop(['year', 'leagueID'], axis=1)

# 5. Rename date column in games to gameDate
games = games.rename(columns={'date': 'gameDate'})

# 6. Drop unnecessary game columns
cols = ['gameID', 'seasonID', 'venueID','gameDate', 'homeGoals', 'awayGoals']
games = games[cols]

# 7. Drop teamID from venue table, convert capacity to integer type
venues = venues.drop('teamID', axis=1)
venues['capacity'] = venues['capacity'].str.replace(',', '')
venues['capacity'] = pd.to_numeric(venues['capacity'], downcast="integer")

# 8. Read in managerTeam table and cast dates to ISO datetime, drop managerName
managerteam['startDate'] = pd.to_datetime(managerteam['startDate'], format='%Y%m')
managerteam['endDate'] = pd.to_datetime(managerteam['endDate'], format='%Y%m', errors='coerce')
managerteam = managerteam.drop('managerName', axis=1)

# 9. Cast season startDate and endDate to ISO datetime, reorder columns to match schema.txt
seasons['startDate'] = pd.to_datetime(seasons['startDate'], format='%Y%m%d')
seasons['endDate'] = pd.to_datetime(seasons['endDate'], format='%Y%m%d')
cols = ['seasonID', 'leagueID', 'championID','year', 'startDate', 'endDate']
seasons = seasons[cols]

# 10. Read in appearances table, select necessary columns, rename shots column to numShots
cols = ['gameID', 'playerID', 'position', 'assists', 'shots', 'goals', 'yellowCard', 'redCard']
appearances = appearances[cols]
appearances = appearances.rename(columns={'shots': 'numShots', 'yellowCard': 'yellowCards', 'redCard': 'redCards'})

11. Read in Shot table, add row index as column shotID, select necessary columns, rename assisterID to assistID
shots['shotID'] = shots.index
cols = ['shotID', 'gameID', 'shooterID', 'assisterID', 'situation', 'shotType', 'shotResult']
shots = shots[cols]
shots = shots.rename(columns={'assisterID': 'assistID'})

# 12. Read in remaining tables, write all tables out to CSV files
leagues = leagues.rename(columns={'name': 'leagueName'})




# ======== Write Final Tables ======================
tables = [gameteam, games, teams, venues, managerteam, seasons, appearances, shots, players, managers, leagues]
names = ['gameteam', 'game', 'team', 'venue', 'managerteam', 'season', 'appearance', 'shot', 'player', 'manager', 'league']
for table, name in zip(tables, names):
    table.to_csv('finalTables/{}.csv'.format(name), index=False)
    
# shots.to_csv('finalTables/shot.csv', index=False)