# URLs
sullygnome = 'https://sullygnome.com/channelsearch/'

# IDs
online_now = 'chkOnlineOnly'
mature = 'chkMature'
language_select = 'ddlLanguage'
search_btn = 'btnSearchChannels'
pages_text = 'tblControl_info'
next_page = 'tblControl_next'

# XPATHs
eng = '//*[@id="ddlLanguage"]/option[12]'
results_page = '//*[@id="tblControl_length"]/label/select/option[4]'


def avg_viewrs(param, type):
    i = [0, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 7500, 10000, 25000]
    x = i.index(int(param))
    return f'//*[@id="ddl{ type }Viewers"]/option[{x + 1}]'


def streamed_hours(param):
    i = [0, 5, 10, 15, 20, 25, 30, 50, 75, 100, 250]
    x = i.index(int(param))
    return f'//*[@id="ddlMinHours"]/option[{ x + 1 }]'
