import os
from .limb_interface import Limb
from typing import Dict, Any

class RenameFileLimb(Limb):
    def __init__(self, name='rename_file'):
        super().__init__(name)

    def actuate(self, params: Dict[str, Any]) -> bool:
        src = params.get('src')
        dst = params.get('dst')
        if not src or not dst:
            raise ValueError('src and dst parameters are required')
        os.rename(src, dst)
        return True 