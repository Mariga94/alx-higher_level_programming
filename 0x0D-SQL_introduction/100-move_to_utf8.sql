-- converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;
