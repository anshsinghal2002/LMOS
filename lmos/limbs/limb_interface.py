from abc import ABC, abstractmethod
from typing import Dict, Any

class Limb(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def actuate(self, params: Dict[str, Any]) -> Any:
        pass 