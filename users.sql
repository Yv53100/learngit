CREATE DATABASE IF NOT EXISTS user;
USE user;
CREATE TABLE IF NOT EXISTS app01_userinfo(id  INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(32),password VARCHAR(64),account VARCHAR(20));
INSERT INTO app01_userinfo VALUES (1,'张三','123456','1234567890');
INSERT INTO app01_userinfo VALUES (2,'李四','654321','2345678901');
