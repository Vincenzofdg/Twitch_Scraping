from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from re import search
from helper.selenium_functions import xpath, social_link

# FireFox settings
setting = Options()
setting.add_argument("--disable-extensions")
setting.add_argument("--disable-gpu")
setting.add_argument("--no-sandbox")
setting.add_argument("--disable-dev-shm-usage")
setting.add_argument("--headless")

web = webdriver.Firefox(options=setting)

twitch_social_medias_block = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div"
twitch_not_now = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div"
twitter_about = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div"

def twitter(url, loop):
    web.get(url + "/about")

    link = social_link('twitter', web)

    if link is False:
        return False

    try:
        web.get(link)

        navigation = web.window_handles
        web._switch_to.window(navigation[-1])

        if loop == 1:
            not_now = xpath(twitch_not_now, web)
            not_now.click()

        about = xpath(twitter_about, web)
        spans = about.find_elements(By.XPATH, "./span")

        for span in spans:
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            email = search(regex, span.text)

            if email:
                return email.group(0)
        return False
    except TimeoutException:
        return False
    except WebDriverException:
        return False
