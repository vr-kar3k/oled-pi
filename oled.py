
import time
import board
import psutil
import socket
import busio
import digitalio
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import subprocess

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 32
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype('PixelOperator.ttf', 16)

# Functions to gather system info
def get_ip(interface):
    try:
        if interface == 'eth0':
            ip = subprocess.getoutput("hostname -I | awk '{print $1}'")
        elif interface == 'wlan0':
            ip = subprocess.getoutput("hostname -I | awk '{print $2}'")
        else:
            ip = "No IP"
    except:
        ip = "No IP"
    return ip

def get_hostname():
    return socket.gethostname()

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent}%"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return f"{disk.percent}%"

def get_temp():
    temp = subprocess.getoutput("vcgencmd measure_temp").replace("temp=", "").replace("'C", "")
    return temp

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return uptime_string

def get_logged_users():
    users = subprocess.getoutput("who | wc -l")
    return users

# Display loop with pages
page = 0
try:
    while True:
        # Clear the image
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        
        # Get system information
        lan_ip = get_ip('eth0')
        wifi_ip = get_ip('wlan0')
        hostname = get_hostname()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        temperature = get_temp()
        uptime = get_uptime()
        logged_users = get_logged_users()
        
        # Page 0: IP,
        if page == 0:
            draw.text((0, 0), f"L-IP: {lan_ip}", font=font, fill=255)
            draw.text((0, 17), f"W-IP: {wifi_ip}", font=font, fill=255)
                      
            
        # Page 1: Hostname, Uptime,
        elif page == 1:
            draw.text((0, 0), f"Host: {hostname}", font=font, fill=255)
            draw.text((0, 17), f"Temp: {temperature}C", font=font, fill=255)
        
        # Page 2: RAM Usage, Disk Usage,
        elif page == 2:
            draw.text((0, 0), f"RAM: {memory_usage}", font=font, fill=255)
            draw.text((0, 17), f"Disk: {disk_usage}", font=font, fill=255)
            
        # Page 3: Uptime and logged in users
        elif page == 3:
            draw.text((0, 0), f"Uptime: {uptime}", font=font, fill=255)
            draw.text((0, 17), f"Users: {logged_users}", font=font, fill=255)
            
        
        # Display image
        oled.image(image)
        oled.show()
        
        # Cycle to the next page every 5 seconds
        page = (page + 1) % 4  # Change 3 to the number of pages
        time.sleep(2)
        
except KeyboardInterrupt:
    oled.fill(0)
    oled.show()