CREATE DATABASE log_in;

USE log_in;

CREATE TABLE user_account (
	id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    u_password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);