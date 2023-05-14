from openpyxl import Workbook
from os import system
from helper.text_functions import inject
from web_scraping.twitter import twitter
from web_scraping.instagram import instagram

def no_emails(file):
    emails = open(f"./documents/{file}", mode="r")
    content = emails.read()
    users = content.split("+")
    users.pop(-1)
    emails.close()

    return users


def twitter_scan(txt01, txt02):
    file_02_1 = Workbook()
    twitter_xlsx = file_02_1.active

    not_founded_txt = open(f"./documents/{txt02}", mode="w")
    not_founded, founded, loop = 0, 1, 1

    system('clear')

    inject(twitter_xlsx, ["User", "Viewers", "Link", "Email"], 1)

    print(f'\nScraping Twitter...\n')

    users_with_no_email = no_emails(txt01)

    for user in users_with_no_email:
        porcent = loop / len(users_with_no_email) * 100
        print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")
        user_array = user.split(",")

        email = twitter(user_array[2], loop)

        if email is False:
            not_founded += 1
            line = f"{user_array[0]},{user_array[1]},{user_array[2]}+"
            not_founded_txt.writelines(line)
        else:
            founded += 1
            inject(twitter_xlsx, [*user_array, email], founded)
        loop += 1
    
    file_02_1.save(f"./documents/twitter.xlsx")
    not_founded_txt.close()

    return ['TWITTER', loop, founded, not_founded]


def instagram_scan(txt01, txt02):
    file_02_2 = Workbook()
    instagram_xlsx = file_02_2.active

    not_founded_txt = open(f"./documents/{txt02}", mode="w")
    not_founded, founded, loop = 0, 1, 1

    system('clear')

    inject(instagram_xlsx, ["User", "Viewer", "Link", "Email"], 1)

    print(f'\nScraping Instagram...\n')

    users_with_no_email = no_emails(txt01)

    for user in users_with_no_email:
        porcent = loop / len(users_with_no_email) * 100
        print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")
        user_array = user.split(",")

        email = instagram(user_array[2], loop)
            
        if email is False:
            not_founded += 1
            line = f"{user_array[0]},{user_array[1]},{user_array[2]}+"
            not_founded_txt.writelines(line)
        else:
            founded += 1
            inject(instagram_xlsx, [*user_array, email], founded)
        loop += 1
    
    not_founded_txt.close()

    file_02_2.save(f"./documents/instagram.xlsx")

    return ['INSTAGRAM', loop, founded, not_founded]
