#!/usr/bin/python3
import importlib.util
if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", file_name)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    file_name = 'hidden_4.pyc'
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
