import uos
uos.sdconfig(uos.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
uos.mountsd()
