# main.py

from distutils.log import error
from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys 
import chromedriver_binary  # Adds chromedriver binary to path

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

# Initialize a new browser
try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    sys.stdout.write("selenium has been initiated")
except(error):
    sys.stdout.write("There was a problem with selenium .... again")


@app.route("/")
def hello_world():
    # browser.get("https://fonq.nl/merken")
    browser.get("https://www.google.com/search?q=headless+horseman&tbm=isch")
    browser.save_screenshot("spooky.png")
    return send_file("spooky.png")