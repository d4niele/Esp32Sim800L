# Esp32Sim800L
Prototipo per connettere la schedina ESP32 a internet attraverso un modulo SIM800L  
Connetto il modulo SIM800L alla seconda seriale dell'esp32 (e utilizzo una SIM dati vodafone). Flasho sulla schedina ESP32 la versione di Micropython  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo che include il modulo gsm.
Utilizzo il seguente codice per testare:  

'''python
import gsm
gsm.start(tx=17,rx=16,apn="mobile.vodafone.it")
gsm.ifconfig()
gsm.status()
gsm.start(tx=17,rx=16,apn="mobile.vodafone.it")
gsm.connect()
gsm.status()
gsm.ifconfig()
'''

Se invece voglio solo mandare sms lo posso fare anche utilizzando la versione ufficiale di micropython:  

'''python
from machine import UART
import time
ser = UART(2, 9600)
ser.init(9600, bits=8, parity=None, stop=1)

def sendsms(to, message):
    ser.write('ATZ\r')
    time.sleep(1)
    ser.write('AT+CMGF=1\r')
    time.sleep(1)
    ser.write('''AT+CMGS="''' + to + '''"\r''')
    time.sleep(1)
    ser.write(message + "\r")
    time.sleep(1)
    ser.write(chr(26))
    time.sleep(1)
'''


https://www.treccarichi.net/2016/06/sim800l/  
https://www.instructables.com/id/ESP32-SIM800L-and-Barrier-Sensor/  
https://articulo.mercadolibre.com.co/MCO-487675426-modulo-celular-gsm-gprs-esp800l-sim800l-sim800-arduino-5v-_JM  
https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/  
