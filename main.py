from time import sleep_ms, sleep
from machine import Pin, I2C
import ssd1306
import network

import config


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.WLAN_CONFIG['ssid'], config.WLAN_CONFIG['password'])
        while not wlan.isconnected():
            pass
    # print('network config:', wlan.ifconfig())
    return wlan.ifconfig()


i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Connecting...", 0, 0)
oled.show()

buf = do_connect()
oled.text(buf[0], 0, 16)
oled.text(buf[1], 0, 24)
oled.text(buf[2], 0, 32)

oled.show()

for i in range(0, 10):
    oled.text(str(i), i * 11, 48)
    oled.show()
