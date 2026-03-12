#/usr/bin/env python 
import time 
import board 
import adafruit_sht31d
from Adafruit_I0 import Client, Feed, RequestError

i2c= board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

ADAFRUIT_IO_KEY = '*********'
ADAFRUIT_IO_USERNAME = '********'
#Replace stars with your own IO key and username
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
	temperature_feed = aio.feeds('temperature')
except RequestError:
	feed_temp = Feed(name="temperature")
	temperature_feed = aio.create_feed(feed_temp)

try:
	humidity_feed = aio.feeds('humidity')
except RequestError:
	feed_humid = Feed(name="humidity")
	humidity_feed = aio.create_feed(feed_humid)

temperature = sensor.temperature
humidity = sensor.relative_humidity
temperature = temperature * 9.0 / 5.0 + 32.0
print ('Temp={0:0.1f}*F'.format(temperature))
print ('Humidity={0:0.1f}%'.format(humidity))
temperature = '%.2f'%(temperature)
humidity = '%.2f %(humidity)
aio.send(temperature_feed.key, str(temperature)) 
aio. send(humidity_feed.key, str(humidity))
