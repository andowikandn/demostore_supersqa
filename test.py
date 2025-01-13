
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

def find_element():
    pass
def click_button():
    pass
def input_field():
    pass

#add to cart
driver.get("http://demostore.supersqa.com/")
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div/div/div[2]/main/ul/li[1]/a[1]/img")
click_button.click()
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div[2]/main/div[2]/div[2]/form/button")
click_button.click()
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div[1]/div/a")
click_button.click()

#wrong coupun
input_field = driver.find_element(By.XPATH, '//*[@id="coupon_code"]')
input_field.send_keys("xxx")
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[2]/td/div/button")
click_button.click()

#checkout
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/div[2]/div/div/a")
click_button.click()

#login first to checkout
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div/main/article/div/div/div[2]/div/a")
click_button.click()

#click login without fill
click_button = driver.find_element(By.XPATH, 
    value="/html/body/div[2]/div[2]/div/div/main/article/div/div/form[1]/p[4]/button")
click_button.click()