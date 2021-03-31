from splinter import Browser
import time
from datetime import datetime, timedelta

browser = Browser('chrome')  # defaults to firefox
#browser.driver.maximize_window()
browser.visit('https://devweb.xms.dfds.com/')
print("browser acıldı")
