from pandas import read_excel, concat

# monday = read_excel('documents/final/monday.xlsx')
# tuesday = read_excel('documents/final/tuesday.xlsx')
# wednesday = read_excel('documents/final/wednesday.xlsx')
thursday = read_excel('documents/final/thursday.xlsx')
friday = read_excel('documents/final/friday.xlsx')
# saturday = read_excel('documents/final/saturday.xlsx')
sunday = read_excel('documents/final/sunday.xlsx')

# to_concat = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
to_concat = [thursday, friday, sunday]

result = concat(to_concat, ignore_index=True)

result.drop_duplicates(keep='first', inplace=True)

result.to_excel('final_emails.xlsx', index=True)

