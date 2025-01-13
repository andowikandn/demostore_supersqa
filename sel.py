from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()

def element():
    pass 
def input_field():
    pass
def click_button():
    pass

#positive case
driver.get("https://the-internet.herokuapp.com/login")
input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
input_field.send_keys("tomsmith")
input_field = driver.find_element(By.XPATH, '//*[@id="password"]')
input_field.send_keys("SuperSecretPassword!")
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div/div/form/button")
click_button.click()
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div/div/a/i")
click_button.click()

#negative case
driver.get("https://the-internet.herokuapp.com/login")
input_field = driver.find_element(By.XPATH, '//*[@id="username"]')
input_field.send_keys("xxx")
input_field = driver.find_element(By.XPATH, '//*[@id="password"]')
input_field.send_keys("xxx")
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div/div/form/button")
click_button.click()

#footer click
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[3]/div/div/a")
click_button.click()
