# The intent of this test case is to use three variables to create a valid triangle

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def create_triangle(driver):
    side_length_a = 5
    side_length_b = 8
    side_length_c = 6

    driver.find_element(By.NAME, "side1").send_keys(side_length_a)
    driver.find_element(By.NAME, "side2").send_keys(side_length_b)
    driver.find_element(By.NAME, "side3").send_keys(side_length_c)
    driver.find_element(By.ID, "identify-triangle-action").click()

def main():
    driver = webdriver.Firefox()
    driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
    create_triangle(driver)
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()