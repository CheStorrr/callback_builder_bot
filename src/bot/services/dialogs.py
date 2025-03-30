import json 
from typing import (
    Dict,
    Optional    
)

class DialogReader:

    def __init__(
        self,
        path_to_dialogs: str = "dialogs.json"        
    ):
        self.dialogs = {}
        with open(path_to_dialogs, 'r') as file:
            self.dialogs: Dict[str, str] = json.load(file)
            

        self._answer = None

    def get_dialog(
        self,
        trigger: str 
    ) -> Optional[str]:
        
        self._answer = self.dialogs.get(trigger)
        return self.dialogs.get(trigger)
    
    @property
    def answer(self):
        return self._answer