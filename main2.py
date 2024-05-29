import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Open browser
driver = webdriver.Chrome()
time.sleep(5)


# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
# Maximiza la ventana del navegador
driver.maximize_window()
time.sleep(5)

