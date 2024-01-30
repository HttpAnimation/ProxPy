import os
import json
from selenium import webdriver

script_directory = os.path.dirname(os.path.abspath(__file__))

proxys_file_path = os.path.join(script_directory, 'proxys.json')
with open(proxys_file_path, 'r') as json_file:
    data = json.load(json_file)
    PROXY = data.get('proxy', '')

url_file_path = os.path.join(script_directory, 'url.json')
with open(url_file_path, 'r') as json_file:
    data = json.load(json_file)
    URL = data.get('url', '')

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)

chromedriver_path = os.path.join(script_directory, 'chromedriver')
options.add_argument('executable_path=%s' % chromedriver_path)

driver = webdriver.Chrome(options=options)

driver.get(URL)
driver.quit()