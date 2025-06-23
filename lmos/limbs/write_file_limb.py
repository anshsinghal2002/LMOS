from .limb_interface import Limb
from typing import Dict, Any

class WriteFileLimb(Limb):
    def __init__(self, name='write_file'):
        super().__init__(name)

    def actuate(self, params: Dict[str, Any]) -> bool:
        path = params.get('path')
        content = params.get('content')
        if not path or content is None:
            raise ValueError('path and content parameters are required')
        with open(path, 'w') as f:
            f.write(content)
        return True 