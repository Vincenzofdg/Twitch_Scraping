from datetime import datetime

def day():
    today = datetime.now()
    day_name = today.strftime('%A')
    formated = day_name.lower()

    return formated
