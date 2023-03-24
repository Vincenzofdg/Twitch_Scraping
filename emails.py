from openpyxl import Workbook
from twitch_api.live import streamers_live
from twitch_api.email import get_email
from tools.console import clear
from web_scraping.twitter import twitter

xlsx = Workbook()
document = xlsx.active


def infect(content, line):
    document[f"A{line}"] = content[0]
    document[f"B{line}"] = content[1]
    document[f"C{line}"] = content[2]
    document[f"D{line}"] = content[3]


folder = "./documents"
final_doc = "email.xlsx"
txt_01 = "fase_01.txt"
txt_02 = "fase_02.txt"

infect(["User", "Viewer", "Link", "Email"], 1)
excel_index = 2

info = open(f"{folder}/info.txt", mode="w")

clear()

# Fase 01 => Twitch API Base Info:
not_founded_txt = open(f"{folder}/{txt_01}", mode="w")
not_founded = 0
founded = 0
loop = 1

streamers = streamers_live()

info.writelines(f'Total Streamers: {streamers["Results"]}\n')

for streamer in streamers["Streamers"]:
    porcent = loop / streamers["Results"] * 100
    print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")

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

xlsx.save(f"{folder}/{final_doc}")
not_founded_txt.close()

info.writelines(
    f'From Twitch API found {founded} emails\n -------------------\n')

clear()

# Fase 02 => Getting Twitch API info and searching on twitter:
not_founded_txt = open(f"{folder}/{txt_02}", mode="w")
not_founded = 0
founded = 0
loop = 1
save_at_50 = 50

# Get emails not founded on fase 01 and turn into an array
emails = open(f"{folder}/{txt_01}", mode="r")
content = emails.read()
users_with_no_email = content.split("+")
users_with_no_email.pop(-1)

info.writelines(f'New Total: {len(users_with_no_email)}')

for user in users_with_no_email:
    porcent = loop / len(users_with_no_email) * 100
    print(f"{porcent:.2f}%: Not Founded: {not_founded} | Founded: {founded}")
    user_array = user.split(",")
    link = user_array[2]
    has_on_twitter = twitter(user_array[2], loop)

    if has_on_twitter is False:
        not_founded += 1
        line = f"{user_array[0]},{user_array[1]},{user_array[2]}+"
        not_founded_txt.writelines(line)
    else:
        founded += 1
        infect([*user_array, has_on_twitter], excel_index)
        excel_index += 1
        if founded == save_at_50:
            xlsx.save(f"{folder}/{final_doc}")
            save_at_50 += 20
    loop += 1

xlsx.save(f"{folder}/{final_doc}")
not_founded_txt.close()
emails.close()

info.writelines(f'From Twitter found {founded} emails\n -------------------\n')
