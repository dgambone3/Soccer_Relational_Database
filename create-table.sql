heroku pg:psql -a damp-eyrie-64951

-- \copy manager FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\manager.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
-- \copy managerteam FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\managerteam.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy appearance FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\appearance.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy game FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\game.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
-- \copy team FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\team.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy gameteam FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\gameTeam.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy shot FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\shot.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
-- \copy venue FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\venue.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
-- \copy league FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\league.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy season FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\season.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);
\copy player FROM C:\Users\lurgi\Documents\GitHub\database-grad-project-fall-22\finalTables\player.csv WITH (FORMAT CSV, DELIMITER ',', HEADER true);


