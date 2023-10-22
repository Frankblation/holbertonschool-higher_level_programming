-- SQL Script to create the force_name table in the specified database
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
