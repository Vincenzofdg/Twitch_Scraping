from os import system
from openpyxl import Workbook
from twitch_api.live import streamers_live
from twitch_api.email import get_email
from helper.text_functions import inject

def base_search(txt):
    file_01 = Workbook()
    twitch_xlsx = file_01.active

    not_founded_txt = open(f"./documents/{txt}", mode="w")
    not_founded, founded, loop = 0, 1, 1

    system('clear')

    inject(twitch_xlsx, ["User", "Viewers", "Link", "Email"], 1)

    print('\nGetting info from Twitch API...\n')

    streamers = streamers_live()

    for streamer in streamers["Streamers"]:
        porcent = loop / streamers["Results"] * 100
        print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded - 1}")

        email = get_email(streamer[0])

        if email:
            founded += 1
            inject(twitch_xlsx, [*streamer, email], founded)
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

    file_01.save(f"./documents/twitch_api.xlsx")
    not_founded_txt.close()

    return ['TWITCH API', loop, (founded - 1), not_founded]