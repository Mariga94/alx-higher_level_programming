# 0x0E. SQL - More queries

## Learning Objectives
Explain:
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a `PRIMARY KEY`
- What's a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Requirements
 - All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
 - All SQL keywords should be in uppercase.

## Install MySQL 8.0 on Ubuntu 20.04 LTS
    $ sudo apt update
    $ sudo apt install mysql-server
    ...
    $ mysql --version
    mysql Ver 8.0.25-0ubunut0.20.04.1 for Linux on x86_64 ((Ubuntu))
    $
### Connect to your MySQL server:
    $ sudo mysql
## How to import a SQL dump
    $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
    Enter password: 
    $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    id  name
    1   Drama
    2   Mystery
    3   Adventure
    4   Fantasy
    5   Comedy
    6   Crime
    7   Suspense
    8   Thriller
    $
## Tasks
0. [0-privileges.sql]()
