from os import system, remove
from subprocess import run
from helper.text_functions import info_line
from helper.email.step_one import base_search
from helper.email.step_two import twitter_scan, instagram_scan
from helper.email.step_four import final_result

info = open(f"./documents/info.txt", mode="w")
txts = ["step_01.txt", "step_02_1.txt", "step_02_2.txt"]

system('clear')

# 1 Step: Search on Twitch API and create a search base
step_01 = base_search(txts[0])
info.writelines(info_line(*step_01))

system('clear')

# 2 Step: Web Scraping
step_02_1 = twitter_scan(txts[0], txts[1])
info.writelines(info_line(*step_02_1))

step_02_2 = instagram_scan(txts[1], txts[2])
info.writelines(info_line(*step_02_2))

info.close()

system('clear')

# 3 Step: Clean
for txt in txts:
    remove(f'./documents/{txt}')

# 4 Step: all .xslx as one .xslx file
final_result()

system('clear')

# 5 Step: Merge all documents into one
run(['python', 'helper/merge_docs.py'])