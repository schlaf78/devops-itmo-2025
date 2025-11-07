CREATE TABLE directors (
  director_id integer PRIMARY KEY,
  director_name varchar(100) NOT NULL
);

CREATE TABLE countries (
  country_id integer PRIMARY KEY,
  country_name varchar(100) NOT NULL
);

CREATE TABLE actors (
  actor_id integer PRIMARY KEY,
  actor_name varchar(100) NOT NULL
);

CREATE TABLE awards (
  award_id integer PRIMARY KEY,
  award_name varchar(100) NOT NULL
);

CREATE TABLE films (
  film_id integer PRIMARY KEY,
  title varchar(150) NOT NULL,
  director_id integer NOT NULL,
  year integer,
  country_id integer,
  budget numeric,
  FOREIGN KEY (director_id) REFERENCES directors(director_id),
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE film_actors (
  film_id integer NOT NULL,
  actor_id integer NOT NULL,
  PRIMARY KEY (film_id, actor_id),
  FOREIGN KEY (film_id) REFERENCES films(film_id),
  FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
);

CREATE TABLE film_awards (
  film_id integer NOT NULL,
  award_id integer NOT NULL,
  PRIMARY KEY (film_id, award_id),
  FOREIGN KEY (film_id) REFERENCES films(film_id),
  FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

