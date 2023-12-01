#!/usr/bin/python3
import dis
import types
if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
    code = file.read()
    module = types.CodeType.from_codelist(code)
    names = set()
    for instruction in dis.get_instructions(module):
        if instruction.opname == 'LOAD_NAME':
            name = instruction.argval
            if not name.startswith('__'):
                names.add(name)
    for name in sorted(names):
        print(name)
