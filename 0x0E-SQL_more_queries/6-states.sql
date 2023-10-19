-- script that creates the database hbtn_0d_usa and the table states

CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;

USE hbtn_0d_usa;

CREATE TABLE states IF NOT EXISTS (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
