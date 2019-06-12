# Esp32Sim800L
Prototipo per connettere la schedina ESP32 a internet attraverso un modulo SIM800L  
 - Connetto il modulo SIM800L alla seriale UART2 dell'ESP32 e inseriscoo una SIM dati vodafone nello slot della SIM800L. 
 - Flasho sulla schedina ESP32 la versione di Micropython  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo che include il modulo gsm.

Utilizzo il seguente codice per testare:  

```python
import gsm
gsm.start(tx=17,rx=16,apn="mobile.vodafone.it") #sostituire eventualmente con i numeri di pin corretti
gsm.ifconfig()
gsm.status()
gsm.connect()
gsm.status()
gsm.ifconfig()
```

Se invece voglio solo mandare sms lo posso fare anche utilizzando la versione ufficiale di micropython:  

```python
from machine import UART
import time
ser = UART(2,  tx=17, rx=16)
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
```

### Link utili
https://www.treccarichi.net/2016/06/sim800l/  
https://www.instructables.com/id/ESP32-SIM800L-and-Barrier-Sensor/  
https://articulo.mercadolibre.com.co/MCO-487675426-modulo-celular-gsm-gprs-esp800l-sim800l-sim800-arduino-5v-_JM  
https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/  
