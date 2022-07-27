#!/bin/bash

clear
echo -e "[*]Instalation\n"

pip3 install colorama
pip3 install webdriver_manager

clear

echo -n "HEY! type the path of your ChromeDriver here-> "
read path

chmod +x $path
sudo mv -f $path /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
