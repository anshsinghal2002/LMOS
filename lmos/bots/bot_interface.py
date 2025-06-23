from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BotInterface(ABC):
    def __init__(self, limbs: List[Any], xml_config: str):
        self.limbs = limbs
        self.xml_config = xml_config

    @abstractmethod
    def limb_actuate(self, limb_name: str, params: Dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def execute_sequence(self):
        pass 