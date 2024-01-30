import os
from selenium import webdriver

PROXY = "149.102.130.120:80"

script_directory = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)

chromedriver_path = os.path.join(script_directory, 'chromedriver')
options.add_argument('executable_path=%s' % chromedriver_path)

driver = webdriver.Chrome(options=options)

driver.get('https://google.com')
driver.quit()
