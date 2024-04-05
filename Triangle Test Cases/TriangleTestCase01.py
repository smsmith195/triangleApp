# The intent of this test case is to use a single variable to create an equilateral triangle
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def set_up_page(driver):
    driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")

def create_triangle(driver):
    sideLength = 5
    driver.find_element(By.NAME, "side1").send_keys(sideLength)
    driver.find_element(By.NAME, "side2").send_keys(sideLength)
    driver.find_element(By.NAME, "side3").send_keys(sideLength)
    driver.find_element(By.ID, "identify-triangle-action").click()

def main():
    driver = webdriver.Firefox()
    set_up_page(driver)
    create_triangle(driver)
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()