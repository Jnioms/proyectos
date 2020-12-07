import machine
import utime
import network
import urequests
import ntptime
import gc

def apretar_boton(numero_pin = 0):
	boton = machine.Pin(numero_pin, machine.Pin.IN, machine.Pin.PULL_UP)
	return boton.value()

def conectar_wlan():
	wlan = network.WLAN(network.STA_IF)
	if not wlan.isconnected():
		wlan.active(True)
		wlan.connect('SSID', 'Password')

def setear_hora(zona=10800):
	ntptime.NTP_DELTA = 3155673600+zona
	ntptime.settime()
	
def enviar_mensaje():
	ts = utime.localtime()
	telemsg1 = str(ts[2]) + "-" + str(ts[1]) + "-" + str(ts[0]) + " " + str(ts[3]) + ":" + str(ts[4]) + ":" + str(ts[5]) + " --- Timbre"
	telemsg2 = urequests.get("https://api.telegram.org/bot*******to:ken*****************/sendMessage?text={}&chat_id=****id****".format(telemsg1))
	telemsg2.close()
	gc.collect()

while True:
	if apretar_boton() == 0:
		try:
			conectar_wlan()
			setear_hora()
			enviar_mensaje()
			utime.sleep(5)
			continue
		except:
			gc.collect()
			conectar_wlan()
			continue