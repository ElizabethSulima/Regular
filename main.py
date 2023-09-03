from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    redact_list = []
pprint(contacts_list)

def names_change():
    pattern_name = r'([А-Я])'
    new_name = r' \1'
    for i in contacts_list[1:]:
        line = i[0] + i[1] + i[2]
        if len((re.sub(pattern_name, new_name, line).split())) == 3:
            i[0] = re.sub(pattern_name, new_name, line).split()[0]
            i[1] = re.sub(pattern_name, new_name, line).split()[1]
            i[2] = re.sub(pattern_name, new_name, line).split()[2]
        elif len((re.sub(pattern_name, new_name, line).split())) == 2:
            i[0] = re.sub(pattern_name, new_name, line).split()[0]
            i[1] = re.sub(pattern_name, new_name, line).split()[1]
            i[2] = ''
        elif len((re.sub(pattern_name, new_name, line).split())) == 1:
            i[0] = re.sub(pattern_name, new_name, line).split()[0]
            i[1] = ''
            i[2] = ''
    return

def formatting_phones():
    pattern_phone = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_sub = r'+7(\2)\3-\4-\5\7\8\9'
    for i in contacts_list:
        i[5] = pattern_phone.sub(phone_sub, i[5])
    return

def editing_list():
    for i in contacts_list[1:]:
        first_name = i[0]
        last_name = i[1]
        for j in contacts_list:
            first_name_new = j[0]
            last_name_new = j[1]
            if first_name == first_name_new and last_name == last_name_new:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    for n in contacts_list:
        if n not in redact_list:
            redact_list.append(n)
    return redact_list

if __name__ == '__main__':
    names_change()
    formatting_phones()
    editing_list()
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(redact_list)