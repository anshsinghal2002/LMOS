import shutil
import os
from .limb_interface import Limb
from typing import Dict, Any

class BackupFolderLimb(Limb):
    def __init__(self, name='backup_folder'):
        super().__init__(name)

    def actuate(self, params: Dict[str, Any]) -> bool:
        src = params.get('src')
        dst = params.get('dst')
        if not src or not dst:
            raise ValueError('src and dst parameters are required')
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        return True 