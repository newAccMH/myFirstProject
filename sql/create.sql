 CREATE DATABASE test_list_db;
 USE test_list_db;
 DROP TABLE IF EXISTS list_table;
 CREATE TABLE list_table (
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);
INSERT INTO list_table (name) VALUES ('Oranges');
INSERT INTO list_table (name) VALUES ('Bananas');
INSERT INTO list_table (name) VALUES ('Pears');