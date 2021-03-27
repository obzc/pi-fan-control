# Raspberry Pi Automated Fan Control
Automated Raspberry Pi Fan Control (python script)


sudo vim /etc/rc.local

screen -L -dmS fann python /home/pi/fan.py &

tekrar görüntülemek için
sudo screen -r fann

bütün screenleri görmek için
sudo screen -ls
