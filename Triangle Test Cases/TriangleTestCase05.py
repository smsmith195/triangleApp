# The intent of this test case is to intentionally cause an error by using non-numerical values in the triangle app

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def create_triangle(driver):
    sideLengthA = "asdf"
    sideLengthB = "!£$%"
    sideLengthC = "дождь"

    driver.find_element(By.NAME, "side1").send_keys(sideLengthA)
    driver.find_element(By.NAME, "side2").send_keys(sideLengthB)
    driver.find_element(By.NAME, "side3").send_keys(sideLengthC)
    driver.find_element(By.ID, "identify-triangle-action").click()

def main():
    driver = webdriver.Firefox()
    driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
    create_triangle(driver)
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()