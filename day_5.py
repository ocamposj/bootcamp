def space():
    print("--------------------------------------------------------------------------------")

import RPi.GPIO as gpio #libreria para puertos
import Adafruit_DHT as dht
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25

gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

led_list = [led_r,led_y,led_g]
led_time = 0.05

# def sequence1():
# 	led_list = [led_r,led_y,led_g]
# 	led_time = 0.07
# 	while True:
# 		for led_on in led_list:
# 			gpio.output(led_on,True)
# 			sleep(led_time)
# 		for led_off in led_list:
# 			gpio.output(led_off,False)
# 			sleep(led_time)

# def sequence2():
# 	led_list = [led_r,led_y,led_g]
# 	led_time = 0.07
# 	while True:
# 		for led_on in led_list:
# 			gpio.output(led_on,True)
# 			sleep(led_time)
# 			gpio.output(led_on,False)
# 			sleep(led_time)

# while True:
# 	for led_on in led_list:
# 		gpio.output(led_on,True)
# 		sleep(led_time)
# 	for led_off in led_list:
# 		gpio.output(led_off,False)
# 		sleep(led_time)


# cont = 0
# while True:
# 	print(cont)
# 	if gpio.input(led_s):
# 		cont = cont + 1
# 		sleep(0.3)
# 		if cont == 4:
# 			cont = 0
# 	if cont == 0:
# 		gpio.output(led_r,False)
# 		gpio.output(led_y,False)
# 		gpio.output(led_g,False)
	
# 	if cont == 1:
# 		gpio.output(led_r,True)
# 		gpio.output(led_y,False)
# 		gpio.output(led_g,False)
	
# 	if cont == 2:
# 		gpio.output(led_r,False)
# 		gpio.output(led_y,True)
# 		gpio.output(led_g,False)
	
# 	if cont == 3:
# 		gpio.output(led_r,False)
# 		gpio.output(led_y,False)
# 		gpio.output(led_g,True)


def DHT11_data():
	humi, temp = dht.read_retry(dht.DHT11, 18)
	return humi, temp
	
# while True:
# 	try:
# 		humedad, temperatura = DHT11_data()
# 		if humedad is not None and temperatura is not None:
# 			print("Humedad:", humedad, "Temperatura", temperatura)
# 		else:
# 			print("Error en la lectira del sensor")
# 		sleep(20)
# 	except KeyboardInterrupt:
# 		gpio.clean()
# 		print("Programa terminado")
# 		break

while True:
	try:
		humedad, temperatura = DHT11_data()
		print("Humedad:", humedad, "Temperatura", temperatura)
        if humedad > 50.0:
			gpio.output(led_r, True)
            gpio.output(led_g, False)
		else:
			gpio.output(led_r, False)
            gpio.output(led_g, True)
		sleep(20)
	except KeyboardInterrupt:
		gpio.clean()
		print("Programa terminado")
		break