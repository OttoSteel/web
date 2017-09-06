#sudo rm -r /etc/mysql/my.cnf
#sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
sudo /etc/init.d/mysql start

mysql -u root -e "CREATE DATABASE qa"/*!40100 DEFAULT CHARACTER SET utf8 */ ; 
mysql -u root -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
				 GRANT ALL PRIVILEGES ON qa.* TO 'qauser'@'localhost';"
