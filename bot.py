from selenium import webdriver
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from math import ceil
import elem

env = dotenv_values('.env')


def id(param): return web.find_element(By.ID, param)


def className(param): return web.find_element(By.CLASS_NAME, param)


def xpath(param): return web.find_element(By.XPATH, param)


if env['browser'] == 'Firefox':
    web = webdriver.Firefox()
if env['browser'] == 'Chrome':
    web = webdriver.Chrome()
if env['browser'] == 'Edge':
    web = webdriver.Edge()
elif env['browser'] == 'Safari':
    web = webdriver.Safari()

web.get(elem.sullygnome + env['search_days'])

sleep(2)

# Settings
online_now = id(elem.online_now)
mature = id(elem.mature)
select_eng = xpath(elem.eng)
avg_min = xpath(elem.avg_viewrs(env['avg_min'], 'Min'))
avg_max = xpath(elem.avg_viewrs(env['avg_max'], 'Max'))
streamed_hours = xpath(elem.streamed_hours(env['streamed_hours']))
results_page = xpath(elem.results_page)
search_btn = id(elem.search_btn)

online_now.click()
mature.click()
select_eng.click()
avg_min.click()
avg_max.click()
streamed_hours.click()
results_page.click()
search_btn.click()

sleep(15)  # Timer problematico

pages_text_html = id(elem.pages_text)
pages_text = pages_text_html.text
text_array = pages_text.split(' of ')
array_pages = text_array[1].split(' ')
text = array_pages[0]
num_of_users = text.replace(",", "")

pages = ceil(int(num_of_users) / 100) + 1

# Page 01
file = open('data.txt', mode='w')
file.writelines(
    'User Name | Stream Time | Peak Viewers | Average Viewers | Twitch Link\n\n')

for page in range(1, pages):
    next_page = id(elem.next_page)
    file.writelines(f'\n\n---------------- Page {page} ----------------\n\n')

    for i in range(1, 101):
        base = f'//*[@id="tblControl"]/tbody/tr[{i}]'
        username = xpath(f'{base}/td[3]/a')
        stream_time = xpath(f'{base}/td[5]/div/div/div')
        peak_viewers = xpath(f'{base}/td[6]/div/div/div')
        avg_viewers = xpath(f'{base}/td[7]/div/div/div')
        twitch_link = xpath(f'{base}/td[12]/a')

        link = twitch_link.get_attribute('href')
        try:
            line = f'[{i}] {username.text} | {stream_time.text} | {peak_viewers.text} | {avg_viewers.text} | {link}\n'
            file.writelines(line)
        except UnicodeEncodeError:
            line = f'xxxxx | {stream_time.text} | {peak_viewers.text} | {avg_viewers.text} | {link}\n'
            file.writelines(line)

    next_page.click()
    sleep(10)  # Timer problematico


sleep(15)
web.quit()
