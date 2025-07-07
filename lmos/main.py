import sys
import os
from bots.basic_bot import BasicBot
from limbs.rename_file_limb import RenameFileLimb
from limbs.backup_folder_limb import BackupFolderLimb
from limbs.create_file_limb import CreateFileLimb
from limbs.write_file_limb import WriteFileLimb

LIMB_CLASSES = {
    'rename_file': RenameFileLimb,
    'backup_folder': BackupFolderLimb,
    'create_file': CreateFileLimb,
    'write_file': WriteFileLimb,
}

EXAMPLE_LAUNCH_FILES = [
    'launch_files/rename_file.xml',
    'launch_files/backup_folder.xml',
    'launch_files/create_and_write_file.xml',
]

def main(xml_path):
    bot = BasicBot(xml_path, LIMB_CLASSES)
    bot.execute_sequence()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py <launch_file.xml>')
        print('Example launch files:')
        for f in EXAMPLE_LAUNCH_FILES:
            print(f'  {f}')
        sys.exit(1)
    xml_path = sys.argv[1]
    if not os.path.exists(xml_path):
        print(f'Launch file {xml_path} does not exist.')
        sys.exit(1)
    main(xml_path) 