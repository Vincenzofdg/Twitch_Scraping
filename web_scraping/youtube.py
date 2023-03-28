from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from time import sleep
from re import search
# from .tools import xpath
from tools import xpath

# FireFox settings
# setting = Options()
# setting.add_argument("--disable-extensions")
# setting.add_argument("--disable-gpu")
# setting.add_argument("--no-sandbox")
# setting.add_argument("--disable-dev-shm-usage")
# setting.add_argument("--headless")

# web = webdriver.Firefox(options=setting)
web = webdriver.Firefox()

twitch_social_medias_block = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div"
twitch_not_now = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div"

click_here_to_see_the_email = '//*[@id="details-container"]/table/tbody/tr[1]/td[3]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'
recaptcha = '//*[@id="recaptcha-anchor"]/div[1]'
send_btn = '//*[@id="submit-btn"]/span/yt-formatted-string'
email_link = '//*[@id="email"]'


def use_youtube():
    try:
        all_social_media = xpath(twitch_social_medias_block, web)
        medias = all_social_media.find_elements(By.XPATH, "./*")
        i = 1
        for _ in medias:
            path = f"/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div/a"
            media = xpath(path, web)
            link = media.get_attribute("href")

            if "youtube" in link:
                return link
            else:
                i += 1
        return False
    except TimeoutException:
        return False


def youtube(url, loop):
    web.get(url + "/about")

    # if loop == 1:
    #     sleep(15)
    #     not_now = xpath(twitch_not_now, web)
    #     not_now.click()

    youtube_link = use_youtube()

    if youtube_link is False:
        return False

    try:
        web.get(youtube_link + "/about")

        navigation = web.window_handles
        web._switch_to.window(navigation[-1])

        # to_see_email = xpath(click_here_to_see_the_email, web)
        # to_see_email.click()

        # i_am_not_a_robot = xpath(recaptcha, web)
        # i_am_not_a_robot.click()

        # sleep(3)

        send = xpath(send_btn, web)
        send.click()

        email = xpath(email_link, web)
        result = email.text

        print(result)
        return result
    except TimeoutException:
        return False
    except WebDriverException:
        return False


youtube('https://www.twitch.tv/gaules', 1)

# Problema 01: Verificador de robo
# Problema 02: email so visivel se estiver logado, email publico?
# Problema 03: Limite de de visualizacao