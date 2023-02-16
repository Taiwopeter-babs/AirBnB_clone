#!/usr/bin/python3
import re


def process(text):
    new = []
    res = [arg for arg in re.split(r'[\[\]().,]', text) if arg.strip()]
    for arg in res:
        arg = arg.strip(" ")
        new.append(arg)
    return new

text = "User.update('38f22813-2753-4d42-b37c-57a17f1e4f88', {'first_name': 'John', 'age': 89})"
res = re.search('(?<=\s).*}', text)
to_dict = eval(res.group(0))
print(to_dict, type(to_dict))
print("============")
res = process(text)
print(res)

text = "User.update('38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name, 'John')"
res = process(text)
