from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import signal

logging.basicConfig(
		format='%(asctime)s %(levelname)-8s %(message)s',
		level=logging.INFO,
		datefmt='%Y-%m-%d %H:%M:%S')

logging.info("LAUNCH")
firefox_options = webdriver.FirefoxOptions()

def alarm_handler(signum, frame):
	raise Exception("Timeout while loading webpage")

signal.signal(signal.SIGALRM, alarm_handler)

while 1:
  # Get a new driver
	time.sleep(5)
	driver = None
	signal.alarm(10)
	try:
		logging.info("Getting webdriver....")
		driver = webdriver.Remote(command_executor="http://firefox:4444/wd/hub", options=firefox_options)
		driver.set_page_load_timeout(5)
		driver.set_script_timeout(5)
		driver.get("http://romweb/messages.php")
		driver.add_cookie({'name' : 'auth', 'value': '663byOdkoUx8FiGsk7goJqSZXhzqgtog5JyLN9AJFsfZCvnas8U3TQjdtGn3gxdWIZRqRbb1YQrZjhqny3skN6J2bu4IjhfMGuA02o'})
		driver.get("http://romweb/messages.php");
		clicks = 0
		try:
			while True: 
				driver.switch_to_alert().accept()
				clicks+=1
				time.sleep(0.1)
		except Exception as e:
			pass
		if clicks:
			logging.info(f" {clicks} accept clicks!")
		driver.quit()
	except Exception as e:
		logging.info("error: " + str(e))
		time.sleep(2)
		try:
			if driver:
				driver.quit()
		except Exception as e:
			logging.error("quitting error: " + str(e))
			pass
	finally:
		signal.alarm(0)
