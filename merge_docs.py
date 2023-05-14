from os import remove
from helper.day import day
from datetime import datetime
from pandas import read_excel, concat, DataFrame
from numpy import array

# today = datetime.now()
# day_name = today.strftime('%A')
# day = day_name.lower()

base = read_excel('documents/emails.xlsx')
new_date = read_excel(f'documents/{day()}.xlsx')

header_model = ['User', 'Viewers', 'Link', 'Email']

to_concat = [base, new_date]

result = concat(to_concat, ignore_index=True)
result.drop_duplicates(keep='first', inplace=True)
result.to_excel('documents/all.xlsx', index=False, header=header_model)

all = read_excel('documents/all.xlsx')

people = array(all)
passed = []
not_passed = []
i = 0

for person in people:
    name = person[0]
    count = 0
    duplicate = False

    for user in people:
        if (user[0] == name):
          if (count > 1):
            duplicate = True
          else:
             count += 1

    if (duplicate is False):
      passed.append(person)

    elif (duplicate is True):
      if len(not_passed) < 1:
        not_passed.append(person)
      else:
        tracker = 0
        for user in not_passed:
          if user[0] == name:
            tracker += 1
        
        if tracker == 0:
          not_passed.append(person)


    i += 1

for elem in not_passed:
  passed.append(elem)

print(f"New result file generated with {len(passed)}")

file = DataFrame(passed)
file.to_excel('documents/emails.xlsx', index=False, header=header_model)

remove('./documents/all.xlsx')
remove(f'./documents/{day()}.xlsx')