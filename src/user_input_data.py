import json
import os
from pathlib import Path
from logger import logger_instance


class UserInput:
    def __init__(self):
        self.json_fn = Path(os.path.abspath(__file__)).parent.parent / 'non_statics' / 'uinp.json'
        with open(self.json_fn, 'r') as fn:
            self.user_dict = json.load(fn)
        
        self.log()
        
    def get_uinp(self) -> dict:
        return self.user_dict.copy()
    
    def log(self):
        '''
        Writes to log any issues I want to check for.
        '''
        grid_cell_size = self.user_dict['grid_cell_size']
        for key in ['width', 'height']:
            # Grid is 32x32. We want to 
            if self.user_dict[key] % grid_cell_size != 0:
                logger_instance.debug(f'{key} is not divisibile by 32. Grid will be funky. Floor: {grid_cell_size * (self.user_dict[key] // grid_cell_size)}, Ceiling : {grid_cell_size * ((self.user_dict[key] // grid_cell_size) + 1)}')
        
