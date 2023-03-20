import openpyxl
from src.api.get_user_email import user_twitch_api

excel = openpyxl.Workbook()
document = excel.active


def file_to_array():
    with open('results/base.txt') as file:
        content = file.read()
        print('aqui')
        array_users = content.split('+')
        array_users.pop(-1)

        return array_users


def excel_infect(param, i):
    document[f'A{i}'] = param[0]
    document[f'B{i}'] = param[1]
    document[f'C{i}'] = param[2]
    document[f'D{i}'] = param[3]
    document[f'E{i}'] = param[4]
    document[f'F{i}'] = param[5]


def email_to_xlsx():
    arrays = file_to_array()
    excel_index = 2
    title_line = ['User Name', 'Stream Time', 'Peak Viewers',
                  'Average Viewers', 'Twitch Link', 'Public Email']
    excel_infect(title_line, 1)

    for array in arrays:
        user = array.split('-')
        email = user_twitch_api(user[0])

        if email:
            add = [*user, f"https://www.twitch.tv/{user}", email]
            excel_infect(add, excel_index)
            excel_index += 1
            print(add)
        else:
            None

    excel.save('./results/scraping.xlsx')


email_to_xlsx()
