from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

limit_time = 11


def id(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.ID, element))
    )


def ids(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_all_elements_located((By.ID, element))
    )


def class_name(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, element))
    )

def name(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.NAME, element))
    )

def css_selector(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.NAME, element))
    )


def xpath(element, browser):
    return wait(browser, limit_time).until(
        EC.presence_of_element_located((By.XPATH, element))
    )


def social_link(media_name, web):
    twitch_social_medias_block = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div"

    try:
        all_social_media = xpath(twitch_social_medias_block, web)
        medias = all_social_media.find_elements(By.XPATH, "./*")
        i = 1
        for _ in medias:
            path = f"/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div/a"
            media = xpath(path, web)
            link = media.get_attribute("href")

            if media_name in link:
                return link
            else:
                i += 1
        return False
    except TimeoutException:
        return False
