# Raspberry Pi Automated Fan Control
Automated Raspberry Pi Fan Control (python script)

![image](https://user-images.githubusercontent.com/5241625/112716699-05c92000-8ef9-11eb-8257-9e97afc8db48.png)



sudo vim /etc/rc.local

screen -L -dmS fann python /home/pi/fan.py &

tekrar görüntülemek için
sudo screen -r fann

bütün screenleri görmek için
sudo screen -ls
