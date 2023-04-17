from pandas import read_excel, concat, DataFrame
from numpy import array

monday = read_excel('documents/final/monday.xlsx')
tuesday = read_excel('documents/final/tuesday.xlsx')
wednesday = read_excel('documents/final/wednesday.xlsx')
thursday = read_excel('documents/final/thursday.xlsx')
friday = read_excel('documents/final/friday.xlsx')
saturday = read_excel('documents/final/saturday.xlsx')
sunday = read_excel('documents/final/sunday.xlsx')

to_concat = [monday, tuesday, wednesday, thursday, friday, sunday]

result = concat(to_concat, ignore_index=True)

result.drop_duplicates(keep='first', inplace=True)

result.to_excel('documents/final/all.xlsx', index=False)

all = read_excel('documents/final/all.xlsx')

people = array(all)
passed = []
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
    i += 1

file = DataFrame(passed)
file.to_excel('result.xlsx', index=True, header=['User', 'Viewers', 'Link', 'Email'])
