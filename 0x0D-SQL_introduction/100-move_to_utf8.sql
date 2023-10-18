-- script that converts hbtn_0c_0 database to UTF8 

ALTER TABLE first_table
  DEFAULT CHARACTER SET utf8mb4,
  MODIFY name CHAR(10)
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
