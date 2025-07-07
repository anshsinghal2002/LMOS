import shutil
import os
from .limb_interface import Limb
from typing import Dict, Any
from datetime import datetime

class BackupFolderLimb(Limb):
    def __init__(self, name='backup_folder', **params):
        super().__init__(name, **params)

    def actuate(self, params: Dict[str, Any]) -> bool:
        merged_params = self.get_params(params)
        src = merged_params.get('src')
        backup_path = merged_params.get('backup_path')
        time_str = merged_params.get('time')
        if not src:
            raise ValueError('src/folder parameter is required')
        if not time_str:
            # fallback to current time if not provided
            time_str = datetime.now().strftime('%Y%m%dT%H%M%S')
        # Create the timestamped subfolder
        dst = os.path.join(backup_path, time_str)
        if not os.path.exists(dst):
            os.makedirs(dst)
        print (src)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        return True 