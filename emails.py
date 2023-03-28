from openpyxl import Workbook
from os import remove
from twitch_api.live import streamers_live
from twitch_api.email import get_email
from tools.console import clear
from web_scraping.twitter import twitter
from web_scraping.instagram import instagram

xlsx = Workbook()
document = xlsx.active

info = open(f"./documents/info.txt", mode="w")
txt_01, txt_02, txt_03 = "fase_01.txt", "fase_02.txt", "fase_03txt"


def infect(content, line):
    document[f"A{line}"] = content[0]
    document[f"B{line}"] = content[1]
    document[f"C{line}"] = content[2]
    document[f"D{line}"] = content[3]


def text_line(name, total, founded, not_founded):
    return f'[{name}] Total: {total} | Emails: {founded} | No Email: {not_founded}\n'


def base_search(txt):
    not_founded_txt = open(f"./documents/{txt}", mode="w")
    not_founded = 0
    founded = 0
    loop = 1
    excel = 1

    clear()

    print('\nGetting info from Twitch API...\n')

    streamers = streamers_live()

    for streamer in streamers["Streamers"]:
        porcent = loop / streamers["Results"] * 100
        print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")

        email = get_email(streamer[0])

        if email:
            infect([*streamer, email], excel)
            excel += 1
            founded += 1
        else:
            not_founded += 1
            try:
                line = f"{streamer[0]},{streamer[1]},{streamer[2]}+"
                not_founded_txt.writelines(line)
            except UnicodeDecodeError:
                None
            except UnicodeEncodeError:
                None

        loop += 1

    xlsx.save(f"./documents/twitch_api.xlsx")
    not_founded_txt.close()

    return ['twitch api', loop, founded, not_founded]


def no_emails(file):
    emails = open(f"./documents/{file}", mode="r")
    content = emails.read()
    users = content.split("+")
    users.pop(-1)
    emails.close()
    return users


def social_network(media, txt01, txt02):
    not_founded_txt = open(f"./documents/{txt02}", mode="w")
    not_founded = 0
    save_at_25 = 25
    founded = 0
    loop = 1
    excel = 1

    clear()

    print(f'\nScraping {media}...\n')

    users_with_no_email = no_emails(txt01)

    for user in users_with_no_email:
        porcent = loop / len(users_with_no_email) * 100
        print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")
        user_array = user.split(",")

        if media == 'twitter':
            email = twitter(user_array[2], loop)
        elif media == 'instagram':
            email = instagram(user_array[2], loop)

        if email is False:
            not_founded += 1
            line = f"{user_array[0]},{user_array[1]},{user_array[2]}+"
            not_founded_txt.writelines(line)
        else:
            founded += 1
            infect([*user_array, email], excel)
            excel += 1
            if founded == save_at_25:
                xlsx.save(f"./documents/{media}.xlsx")
                save_at_25 += 25
        loop += 1
    
    xlsx.save(f"./documents/{media}.xlsx")
    not_founded_txt.close()

    clear()

    return [media, loop, founded, not_founded]


# SCRIPT
fase_01 = base_search(txt_01)
info.writelines(text_line(*fase_01))

fase_02 = social_network('twitter', txt_01, txt_02)
info.writelines(text_line(*fase_02))

fase_03 = social_network('instagram', txt_02, txt_03)
info.writelines(text_line(*fase_03))

info.close()

# FINAL XLSX FILE
# infect(["User", "Viewer", "Link", "Email"], 1)
# xlsx.save("./documents/emails.xlsx")
# remove('./documents/fase_01')
# remove('./documents/fase_02')
# remove('./documents/fase_03')
# remove('./documents/fase_04')

# ver o erro de Workbook ao gerar a planilha do instagram