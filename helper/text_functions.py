def inject(file, content, line):
    file[f"A{line}"] = content[0]
    file[f"B{line}"] = content[1]
    file[f"C{line}"] = content[2]
    file[f"D{line}"] = content[3]


def info_line(name, total, founded, not_founded):
    return f'[{name}] Total: {total} | Emails: {founded} | No Email: {not_founded}\n'
