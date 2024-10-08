## Installation Steps:

1. Connect **GND, VCC(3.3v), SCL, & SDA** ports of the display according to the picture shown below:

<img src="https://www.the-diy-life.com/wp-content/uploads/2021/11/Screenshot-2021-11-14-at-22.16.39-1024x576.jpg">

2. Upgrade your Raspberry Pi firmware and reboot:

```shell
    $ sudo apt-get update
    $ sudo apt-get full-upgrade
    $ sudo reboot
```

3. Install python3-pip & upgrade the setuptools

```shell
    $ sudo apt-get install python3-pip
    $ sudo pip3 install --upgrade setuptools
```

4. Next, we’re going to install the Adafruit CircuitPython library using the following commands:

```shell
    $ cd ~
    $ sudo pip3 install --upgrade adafruit-python-shell
    $ sudo reboot

    $ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    $ sudo python3 raspi-blinka.py
```

5. Check the `I2C` status using the command:

```shell
    $ sudo i2cdetect -y 1

        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --
```

6. Next, we need to install the CircuitPython libraries specific to the display. Start by entering the following commands:

```shell
    $ sudo pip3 install adafruit-circuitpython-ssd1306
    $ sudo pip3 install psutil
    $ sudo reboot
    $ sudo apt-get install python3-pil
```

7. Now we need to download the python script from out github:

```shell
    $ git clone https://github.com/vr-kar3k/oled-pi.git

    $ cd OLED_Stats
    $ cp PixelOperator.ttf ~/PixelOperator.ttf
    $ cp oled.py ~/oled.py

```

8. For activating the `crontab` follow the procedure:

```shell
    $ crontab -e
```

**Add this at the bottom:**

Remember to change your username (pi below) if you're not using the default username

```
    @reboot python3 /home/pi/oled.py &

```

9. At the end DELETE the OLED_Stats folder and reboot

```shell
    $ sudo rm -rf OLED_Stats
    $ sudo reboot
```

## Display Issues:

If your display shows jumbled pixels/symbols instead of actual text - you may have a display which supports the SH1106 driver instead of more common SSD1306 driver. This script ONLY works for SSD1306 displays.
If you have this issue, follow this guide instead: https://www.youtube.com/watch?v=LdOKXUDw2NY

<h3><p align="center">THE  END</p></h3>
