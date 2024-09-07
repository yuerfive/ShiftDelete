# pyinstaller -F --uac-admin main.py --noconsole

import subprocess
from threading import Thread


# 运行 AutoHotkey\AutoHotkeyU64.exe 文件
Thread(target=subprocess.run, args=([r'AutoHotkey\AutoHotkeyU64.exe', r'GetFilePath.ahk'], )).start()

# 运行 DeleteFile.exe 文件
Thread(target=subprocess.run, args=([r'DeleteFile.exe'], )).start()
