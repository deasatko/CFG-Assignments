CREATE DATABASE watchlist;

USE watchlist;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE movie (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    release_year VARCHAR(4) NOT NULL,
    genre VARCHAR(50) NOT NULL
);

CREATE TABLE watchlist (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (movie_id) REFERENCES movie(id),
    UNIQUE (user_id, movie_id)
);

INSERT INTO user (first_name, last_name, email) VALUES
('Martina', 'Zerbi', 'mzerb@outlookk.com'),
('Andrea', 'Silinga', 'asiling@outlookk.com'),
('Giacomo', 'Zucca', 'gzucca@outlookk.com'),
('Francesca', 'Bella', 'fbella@outlookk.com'),
('Michele', 'Bassi', 'mbassi@outlookk.com');

INSERT INTO movie (title, release_year, genre) VALUES
('Gossip Girl', '2012' , 'Drama'),
('Suits', '2019', 'Drama'),
('Dune', '2021', 'Sci-Fi'),
('Sabrina', '2020', 'Teen'),
('Wednesday', '2022', 'Teen');

SELECT * FROM movie
JOIN watchlist ON 
watchlist.movie_id = movie.id WHERE watchlist.user_id = 1 ;

INSERT INTO watchlist (movie_id, user_id) VALUES
(1,1)
