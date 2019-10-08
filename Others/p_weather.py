#!/usr/bin/python
import time
import sys
from flask import Flask, render_template
from sense_hat import SenseHat
import spidev
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')

def index():
	sense = SenseHat()
	sense.clear()
	spi = spidev.SpiDev()
	spi.open(0,0)
	spi.bits_per_word=8
try:
	while True:
		celcius = round(sense.get_temperature(), 1)
		fahrenheit = round(1.8 * celcius + 32, 1)
		humidity = round(sense.get_humidity(), 1)
		pressure = round(sense.get_pressure(), 1)

		acceleration = sense.get_accelerometer_raw()
		x = round(acceleration['x'], 2)
		y = round(acceleration['y'], 2)
		z = round(acceleration['z'], 2)

		return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure, x=x, y=y, z=z)
		
		resp = spi.readbytes(1)[0]
		resp = str(resp)
		f = open('file','w')
		f.write(resp)
		f.close()
   		time.sleep(1)
except KeyboardInterrupt:
	pass
	spi.close()

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

	





