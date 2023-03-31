from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from re import search
from time import sleep
from helper.selenium_functions import xpath, name, social_link
from dotenv import dotenv_values

# FireFox settings
setting = Options()
setting.add_argument("--disable-extensions")
setting.add_argument("--disable-gpu")
setting.add_argument("--no-sandbox")
setting.add_argument("--disable-dev-shm-usage")
setting.add_argument("--headless")

web = webdriver.Firefox(options=setting)
env = dotenv_values('.env')

twitch_not_now = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div"

instagram_about = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]'
instagram_btn = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button'
instagram_not_now = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
instagram_notifications = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

def instagram(url, loop):
    if loop == 1:
        # if is the first search, bot will login in.
        web.get("https://www.instagram.com/")

        login = name("username", web)
        login.send_keys(env["login"])

        password = name("password", web)
        password.send_keys(env["password"])

        btn = xpath(instagram_btn, web)
        btn.click()

        not_now = xpath(instagram_not_now, web)
        not_now.click()

        notifications = xpath(instagram_notifications, web)
        notifications.click()   

        sleep(1)


    web.get(url + "/about")

    link = social_link('instagram', web)

    if link is False:
        return False

    try:
        web.get(link)

        about = xpath(instagram_about, web)
        about_content = about.text

        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        email = search(regex, about_content)

        if email:
            return email.group(0)
        else:
            return False

    except TimeoutException:
        return False
    except WebDriverException:
        return False
