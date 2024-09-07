# pyinstaller -F --uac-admin DeleteFile.py --noconsole

import os
import time
import shutil
import schedule
from threading import Thread

# 临时目录路径
TEMP_DIR = f'{os.getcwd()}\\Temp'

# 创建临时目录
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# 删除文件
def deleteFile():
    shutil.rmtree(TEMP_DIR)
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

# 检查文件夹中是否存在文件或文件夹
def checkFile():
    odlFiles = None
    while True:
        newFiles = os.listdir(TEMP_DIR)
        if newFiles and newFiles != odlFiles:
            schedule.clear()
            schedule.every(60).minutes.do(deleteFile)
            odlFiles = newFiles
        elif not newFiles:
            schedule.clear()
        time.sleep(600)

# 定时任务
def scheduledTasks():
    while True:
        # 检查是否有需要执行的任务
        schedule.run_pending()
        # 一定要设置延迟，不然cpu会被满占
        time.sleep(60)

if __name__ == '__main__':
    Thread(target=checkFile).start()
    Thread(target=scheduledTasks).start()