import gsm,json
from network import mqtt

gsm.debug(True)
gsm.start(tx=17,rx=16,apn="TM",roaming=True,wait=True)
gsm.connect()
gsm.status()
gsm.ifconfig()
client = mqtt("test1","calupietru.duckdns.org",port=1883,user="test1",password="test1")
client.start()
message = {"espid":"Prato","timestamp":None,"temperatura":23,"peso":70.1}
client.publish("/maia/4",json.dumps(message))
client.publish("/maia/4",json.dumps(message))
client.stop()
gsm.disconnect()
