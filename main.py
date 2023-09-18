import csv
import re

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    redact_list = []
    contact_red_list = []
    redact_list_1 = []

def names_change():
    pattern_name = r'([А-Я])'
    new_name = r' \1'
    for element in contacts_list[1:]:
        line = " ".join(element[:3])
        if len((re.sub(pattern_name, new_name, line).split())) == 3:
            element[0] = re.sub(pattern_name, new_name, line).split()[0]
            element[1] = re.sub(pattern_name, new_name, line).split()[1]
            element[2] = re.sub(pattern_name, new_name, line).split()[2]
        elif len((re.sub(pattern_name, new_name, line).split())) == 2:
            element[0] = re.sub(pattern_name, new_name, line).split()[0]
            element[1] = re.sub(pattern_name, new_name, line).split()[1]
            element[2] = ''
        elif len((re.sub(pattern_name, new_name, line).split())) == 1:
            element[0] = re.sub(pattern_name, new_name, line).split()[0]
            element[1] = ''
            element[2] = ''
    return


def formatting_phones():
    pattern_phone = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_sub = r'+7(\2)\3-\4-\5\7\8\9'
    for element in contacts_list:
        element[5] = pattern_phone.sub(phone_sub, element[5])
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
    for sublist in contacts_list:
        if sublist not in redact_list:
            redact_list.append(sublist)
    return

def double(redact_list):
    for line in redact_list:
        contact_red_list.append(line[:7])
    for sublist in contact_red_list:
        if sublist not in redact_list_1:
            redact_list_1.append(sublist)
    return
def add_entry(entry):
    dictionary = {}
    key = entry['f'] + entry['i']
    if key in dictionary:
        existing_entry = dictionary[key]
        for field in entry:
            if field in existing_entry:
                existing_entry[field] += entry[field]
            else:
                existing_entry[field] = entry[field]
    else:
        dictionary[key] = entry



if __name__ == '__main__':
    names_change()
    formatting_phones()
    editing_list()
    double(redact_list)
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(redact_list_1)
