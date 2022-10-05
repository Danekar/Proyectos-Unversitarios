#!/bin/bash
mysql_install_db --user=root
mysqld --user=root & 
sleep 5
mariadb -e " CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';"
mariadb -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'password';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'localhost';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'%';"
mariadb -e "flush privileges;"
mariadb -e "SET @@global.sql_mode= '';"
mariadb -e "CREATE DATABASE youtube;"
mariadb -D youtube -e "create table usuarios(nombrecompl varchar(50), username varchar(20), email varchar(25), passwd varchar(100), PRIMARY KEY (username));"
mariadb -D youtube -e "create table videos(username varchar(20), tagsbusq varchar(10), tamarch varchar(10), filepath varchar(100), fechasubida date, FOREIGN KEY (username) REFERENCES usuarios(username));"
mariadb -D youtube -e "commit;"
apachectl -DFOREGROUND
