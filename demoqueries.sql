-- *Query 1 ("Team Record Ranking"):
SELECT club, wins, losses, draws, 3*wins + draws AS match_points 
FROM (SELECT club1 AS club, SUM(wins) AS wins, SUM(losses) AS losses, SUM(draws) AS draws
		FROM((SELECT T.team_name AS club1, COUNT(G.game_id) AS wins 
				FROM game AS G, team AS T, gameteam AS GT
				WHERE T.team_id = GT.home_team_id
 					AND GT.game_id = G.game_id
 					AND G.home_goals > G.away_goals
				GROUP BY T.team_id
				UNION
				SELECT T.team_name AS club1, COUNT(G.game_id) AS wins 
				FROM game AS G, team AS T, gameteam AS GT
				WHERE T.team_id = GT.away_team_id
 					AND GT.game_id = G.game_id
 					AND G.away_goals > G.home_goals
				GROUP BY T.team_id) AS w
				JOIN (SELECT T.team_name AS club2, COUNT(G.game_id) AS losses 
						FROM game AS G, team AS T, gameteam AS GT
						WHERE T.team_id = GT.home_team_id
 							AND GT.game_id = G.game_id
 							AND G.home_goals < G.away_goals
						GROUP BY T.team_id
						UNION
						SELECT T.team_name AS club2, COUNT(G.game_id) AS losses 
						FROM game AS G, team AS T, gameteam AS GT
						WHERE T.team_id = GT.away_team_id
 							AND GT.game_id = G.game_id
 							AND G.away_goals < G.home_goals
						GROUP BY T.team_id) AS l ON w.club1=l.club2
				JOIN (SELECT T.team_name AS club3, COUNT(G.game_id) AS draws 
						FROM game AS G, team AS T, gameteam AS GT
						WHERE T.team_id = GT.home_team_id
 							AND GT.game_id = G.game_id
 							AND G.home_goals = G.away_goals
						GROUP BY T.team_id
						UNION
						SELECT T.team_name AS club3, COUNT(G.game_id) AS draws 
						FROM game AS G, team AS T, gameteam AS GT
						WHERE T.team_id = GT.away_team_id
 							AND GT.game_id = G.game_id
 							AND G.away_goals = G.home_goals
						GROUP BY T.team_id) AS d on w.club1=d.club3)
		GROUP BY club) AS wld
ORDER BY match_points DESC;

-- !Query 2 ("Teams with the most manager changes"): 
SELECT T.team_name AS Club, COUNT(M.manager_id) AS Managers
FROM Team AS T, Manager AS M, ManagerTeam AS MT
WHERE MT.manager_id = M.manager_id
	AND MT.team_id = T.team_id
GROUP BY T.team_id
ORDER BY Managers DESC;

-- *Query 3("Ranking players by shot conversion percentage"):
SELECT pname AS player, shots AS shots_taken,goals, goals::float/shots::float AS conversion_rate 
FROM((SELECT P.player_name AS pname, P.player_id, SUM(A.num_shots) AS shots 
	FROM Player AS P, Appearance AS A
	WHERE P.player_id = A.player_id
	GROUP BY P.player_id) AS t1
JOIN (SELECT player_id, SUM(goals) AS goals
	 	FROM Appearance
	 	GROUP BY player_id) AS t2
	ON t1.player_id=t2.player_id)
WHERE shots > 50
ORDER BY conversion_rate DESC;

-- *Query 4("Biggest home upsets"):
SELECT    HT.team_name AS home, AT.team_name AS away,V.venue_name AS Location,
	G.game_date AS date, G.home_goals, G.away_goals,
	ABS(G.home_goals - G.away_goals) AS goal_differential
FROM Game AS G
JOIN GameTeam AS GT ON G.game_id = GT.game_id
JOIN Team AS HT ON GT.home_team_id = HT.team_id
JOIN Team AS AT ON GT.away_team_id = AT.team_id
JOIN Venue AS V ON HT.venue_id = V.venue_id
ORDER BY goal_differential DESC LIMIT 20;

-- *Query 5("Ranking teams by championships won"):
SELECT T.team_name, L.league_name AS league, COUNT(S.season_id) AS Championships 
FROM Team AS T, Season AS S, League AS L
WHERE T.team_id = S.champion_id
	AND S.league_id = L.league_id
GROUP BY T.team_id, L.league_name
ORDER BY Championships DESC;

-- *Query 6("Did the pandemic impact the European football seasons?"):
SELECT L.league_name, S.year, COUNT(g.game_id) AS Games_Played, S.end_date - S.start_date AS Days_Duration
FROM League AS L, Game AS G, Season AS S
WHERE L.league_id = S.league_id
	AND G.season_id = S.season_id
GROUP BY S.season_id, L.league_name
ORDER BY league_name;
-- dates algebra (date - date → integer)