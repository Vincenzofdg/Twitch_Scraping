from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from dotenv import dotenv_values
from time import sleep
from math import ceil

import css_elements.sullygnome as elem

# FireFox settings
setting = Options()
setting.add_argument('--disable-extensions')
setting.add_argument('--disable-gpu')
setting.add_argument('--no-sandbox')
setting.add_argument('--disable-dev-shm-usage')
setting.add_argument('--headless')

web = webdriver.Firefox(options=setting)

env = dotenv_values('.env')


def id(param): return wait(web, 10).until(
    EC.presence_of_element_located((By.ID, param)))


def className(param): return wait(web, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, param)))


def xpath(param): return wait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, param)))


web.get(elem.sullygnome + env['search_days'])

sleep(2)

# Settings
online_now = id(elem.online_now)
online_now.click()
mature = id(elem.mature)
mature.click()
select_eng = xpath(elem.eng)
select_eng.click()
avg_min = xpath(elem.avg_viewrs(env['avg_min'], 'Min'))
avg_min.click()
avg_max = xpath(elem.avg_viewrs(env['avg_max'], 'Max'))
avg_max.click()
streamed_hours = xpath(elem.streamed_hours(env['streamed_hours']))
streamed_hours.click()
results_page = xpath(elem.results_page)
results_page.click()
search_btn = id(elem.search_btn)
search_btn.click()


sleep(5)  # Timer problematico

# pages_text_html = id(elem.pages_text)
# pages_text = pages_text_html.text
# text_array = pages_text.split(' of ')
# array_pages = text_array[1].split(' ')
# text = array_pages[0]
# num_of_users = text.replace(",", "")

# pages = ceil(int(num_of_users) / 100) + 1
pages = 13 + 1

users_txt = open('./results/base.txt', mode='w')

for page in range(1, pages):
    next_page = id(elem.next_page)

    print(f"\nPage: {page} of {pages - 1}\n")

    for i in range(1, 101):
        base = f'//*[@id="tblControl"]/tbody/tr[{i}]'

        traking = xpath(f'{base}/td[1]')
        username = xpath(f'{base}/td[3]/a')
        stream_time = xpath(f'{base}/td[5]/div/div/div')
        peak_viewers = xpath(f'{base}/td[6]/div/div/div')
        avg_viewers = xpath(f'{base}/td[7]/div/div/div')

        track = traking.text
        user = username.text
        stream_hts = stream_time.text
        viewers = peak_viewers.text
        avg = avg_viewers.text

        print(f"[{track}] {user}")

        try:
            users_txt.writelines(f"{user}-{stream_hts}-{viewers}-{avg}+")
        except UnicodeEncodeError:
            users_txt.writelines('UnicodeEncodeError Name,')

    next_page.click()
    sleep(10)  # Timer problematico


sleep(5)

web.quit()
