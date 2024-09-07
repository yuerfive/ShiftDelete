# pyinstaller -F --uac-admin MoveFile.py --noconsole

import os
import sys
import shutil

# 临时目录路径
TEMP_DIR = f'{os.getcwd()}\\Temp'

# 创建临时目录
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def moveFile(files):
    for path in files:
        # 获取文件名
        file_name = os.path.basename(path)
        # 目标文件路径
        target_path = f'{TEMP_DIR}\\{file_name}'

        temp_path = None
        if os.path.exists(target_path):
            n = 1
            temp_path = f'{target_path}{n}'
            while os.path.exists(temp_path):
                temp_path = f'{target_path}{n}'
                n += 1

        if temp_path:
            target_path = temp_path
        shutil.move(path, target_path)

# 获取命令行参数
if len(sys.argv) > 1:
    files = sys.argv[1].split('\r\n')
    moveFile(files)