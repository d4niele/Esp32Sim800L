import uos
uos.sdconfig(uos.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=5,maxspeed=16)
uos.mountsd()

import machine, ssd1306
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
oled.text('funziona!!! on', 0, 0)
oled.show()
