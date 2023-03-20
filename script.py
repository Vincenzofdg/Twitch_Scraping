from openpyxl import Workbook

from twitch_api.live import streamers_live
from twitch_api.email import get_email

from tools.console import clear

xlsx = Workbook()
document = xlsx.active


def infect(content, line):
    document[f'A{line}'] = content[0]
    document[f'B{line}'] = content[1]
    document[f'C{line}'] = content[2]
    document[f'D{line}'] = content[3]


path = "./documents"
not_founded = 0
founded = 0
loop = 1
excel_index = 2

infect(['User', 'Viewer', 'Link', 'Email'], 1)
not_founded_txt = open(f'{path}/emails_no_founded.txt', mode='w')

print("\nGetting Info...\n")

streamers = streamers_live()

clear()

print('\n' + str(streamers["Results"]) + ' Streamers Found!')
print("\nChecking Streamers Emails\n")


for streamer in streamers["Streamers"]:
    porcent = loop/streamers["Results"] * 100
    print(f'{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}')

    email = get_email(streamer[0])

    if email:
        infect([*streamer, email], excel_index)
        excel_index += 1
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

xlsx.save(f'{path}/emails_from_twitchAPI.xlsx')
