-- delete the table if it exists
-- first time, we get an error because the table does not exist

DROP TABLE results;
DROP TABLE shootouts;
SET CLIENT_ENCODING TO 'utf8';
-- create tables

CREATE TABLE results (
    date        date,
    home_team   varchar(128),
    away_team   varchar(128),
    home_score  int,
    away_score  int,
    tournament  varchar(128),
    city        varchar(128),
    country     varchar(128),
    neutral     boolean
);

CREATE TABLE shootouts (
    date        date,
    home_team   varchar(128),
    away_team   varchar(128),
    winner      varchar(128)
);


-- load tables

\copy results FROM 'results.csv' DELIMITER ',' CSV HEADER;
\copy shootouts FROM 'shootouts.csv' DELIMITER ',' CSV HEADER;

