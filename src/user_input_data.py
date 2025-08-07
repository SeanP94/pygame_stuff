import json
import os
from pathlib import Path

class UserInput:
    def __init__(self):
        self.json_fn = Path(os.path.abspath(__file__)).parent.parent / 'non_statics' / 'uinp.json'
        with open(self.json_fn, 'r') as fn:
            self.user_dict = json.load(fn)

    def get_uinp(self) -> dict:
        return self.user_dict.copy()