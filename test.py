from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pickle
import os
import pandas as pd
from datetime import datetime, timedelta
import pytesseract
from PIL import Image
import requests
from io import BytesIO
from google.oauth2 import service_account
from googleapiclient.discovery import build


driver = webdriver.Chrome()
url = "https://www.facebook.com/"
driver.get(url)

cookies = pickle.load(open("facebook_cookies_02.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()


time.sleep(50)