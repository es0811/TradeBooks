CREATE USER bookreader WITH PASSWORD 'books123';

DROP DATABASE IF EXISTS BookWorld;

CREATE DATABASE BookWorld;

\c BookWorld

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO bookreader;

---- Tables---

CREATE TABLE Reader(
email varchar(50) NOT NULL,
username varchar(50) NOT NULL,
password varchar(50) NOT NULL,
fname varchar(50) NOT NULL,
lname varchar(50) NOT NULL,
address_line1 varchar(200) NOT NULL,
address_line2 varchar(200),
postal_code varchar(6) NOT NULL,
books_sold integer,
books_rented integer,
books_rented_out integer,
books_purchased integer,
PRIMARY KEY (email),
UNIQUE (username));




CREATE TABLE Book (
book_number SERIAL PRIMARY KEY,
title VARCHAR (200) NOT NULL,
author VARCHAR (200) NOT NULL,
genre VARCHAR (200) NOT NULL,
description VARCHAR (500),
pages integer,
condition VARCHAR(200),
cover VARCHAR(100) NOT NULL,
email VARCHAR(50) NOT NULL,
trade_type VARCHAR(100),
cost integer
);

CREATE TABLE AllTrades (
trade_number SERIAL PRIMARY KEY,
book_number  int NOT NULL,
email VARCHAR(50) NOT NULL,
trade_date DATE NOT NULL
);


ALTER TABLE Book
ADD CONSTRAINT fk_email FOREIGN KEY (email) REFERENCES Reader(email);

ALTER TABLE AllTrades
ADD CONSTRAINT fk_book_num FOREIGN KEY (book_number) REFERENCES Book (book_number),
ADD CONSTRAINT fk_trade_email FOREIGN KEY (email) REFERENCES Reader (email);



 ---Permissions ---

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO bookreader;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO bookreader;
