# Raspberry Pi Automated Fan Control
Automated Raspberry Pi Fan Control (python script)

C: Cpu Temp | F: Fan Status

![image](https://user-images.githubusercontent.com/5241625/112716699-05c92000-8ef9-11eb-8257-9e97afc8db48.png)

`/home/pi` klasörü içine fan.py dosyasını oluşturup repodaki kodları yapıştırın.

Sistem başlangıcında otomatik çalıştırmak için

`sudo vim /etc/rc.local`

`exit 0` kodundan önce aşağıdaki kodu ekleyin

`screen -L -dmS fann python /home/pi/fan.py &`

Önizlemek için için
`sudo screen -r fann`

Bütün screenleri görmek için
`sudo screen -ls`
