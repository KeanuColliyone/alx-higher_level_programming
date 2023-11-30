#!/usr/bin/python3
import types
with open('hidden_4.pyc', 'rb') as file:
    code = file.read()
module = types.CodeType.co_consts[0]
names = [name.decode() for name in module.co_names if not name.startswith('__')]
names.sort()
for name in names:
    print(name)
