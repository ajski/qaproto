from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class Search:

    def nav_bar(self, driver):
        driver.get("https://staging.osf.io/").click()
        driver.find_element_by_xpath("//*[@id="navbarScope"]/div/div[1]/div[1]/a/span[2]/strong").click()