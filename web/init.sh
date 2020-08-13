sudo apt update
sudo apt install python3.8.2
sudo apt-get install -y python3.8.2-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo -H pip3 install --upgrade django
sudo -H pip3 install --upgrade gunicorn
sudo rm  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart 
sudo /etc/init.d/mysql start﻿	