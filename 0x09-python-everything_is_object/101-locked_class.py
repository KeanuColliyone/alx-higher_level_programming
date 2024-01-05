#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            error_msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(error_msg.format(name))
        super().__setattr__(name, value)
