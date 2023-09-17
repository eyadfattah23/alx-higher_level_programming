# Python - Object-relational mapping

## Learning Objectives:

    How to connect to a MySQL database from a Python script

    How to SELECT rows in a MySQL table from a Python script

    How to INSERT rows in a MySQL table from a Python script

    What ORM means

    How to map a Python Class to a MySQL table

    How to create a Python Virtual Environment

## resources:

### venv:

> **youtube**(elzero, some english channels)

> **full_description**(https://realpython.com/python-virtual-environments-a-primer/#treat-them-as-disposables)

### mysqldb(client):

> **summary**:https://www.mikusa.com/python-mysql-docs/row_results.html

### DBS:

1->
```sql
-- Active: 1694358571864@@127.0.0.1@3306@hbtn_0d_tvshows
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

    ```
