#sudo rm -r /etc/mysql/my.cnf
#sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
sudo /etc/init.d/mysql start

mysql -u root -e "CREATE DATABASE qa"; 
mysql -u root -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
GRANT ALL ON qa.* TO 'qauser'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
#mysql -u qauser -e "CREATE DATABASE qa;"
				 
