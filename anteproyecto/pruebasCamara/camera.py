from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview()

for i in range(5):
	sleep(5)
	camera.capture('/home/pi/Pictures/foto%s.jpg' % i)

camera.stop_preview()