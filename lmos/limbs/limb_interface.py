from abc import ABC, abstractmethod
from typing import Dict, Any

class Limb(ABC):
    def __init__(self, name: str, **params):
        self.name = name
        self.params = params or {}

    def get_params(self, action_params: Dict[str, Any]) -> Dict[str, Any]:
        merged = self.params.copy()
        merged.update(action_params)
        return merged

    @abstractmethod
    def actuate(self, params: Dict[str, Any]) -> Any:
        pass 