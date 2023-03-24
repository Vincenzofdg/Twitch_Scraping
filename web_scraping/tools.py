from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

limit_time = 12


def id(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.ID, element))
    )


def ids(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_all_elements_located((By.ID, element))
    )


def className(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.CLASS_NAME, element))
    )


def xpath(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.XPATH, element))
    )
