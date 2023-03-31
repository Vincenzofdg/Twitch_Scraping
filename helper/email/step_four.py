from os import system, remove
from pandas import read_excel, concat

def final_result():
    twitch_path = "./documents/twitch_api.xlsx"
    twitter_path = "./documents/twitter.xlsx"
    instagram_path = "./documents/instagram.xlsx"

    twitch = read_excel(twitch_path)
    twitter = read_excel(twitter_path)
    instagram = read_excel(instagram_path)

    union = concat([twitch, twitter, instagram], axis=0, join="outer")
    union = union.reset_index(drop=True)    
    union.to_excel('./documents/emails.xlsx', index=True)

    system('clear')

    remove(twitch_path)
    remove(twitter_path)
    remove(instagram_path)

    print('\n\nAll the operations have been completed.\n\n\n')

    return
