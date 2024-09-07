# pyinstaller -F --uac-admin main.py --noconsole

import subprocess
from threading import Thread

# 指定AutoHotkey解释器的路径和要运行的.ahk文件路径
ahk_interpreter = r"D:\Program Files\AutoHotkey\AutoHotkeyU64.exe"  # 根据你的安装路径调整
ahk_script = r"GetFilePath.ahk"  # 替换为你的.ahk文件路径

# 指定要运行的.exe文件路径
exe_file = r"DeleteFile.exe"  # 替换为你的.exe文件路径

Thread(target=subprocess.run, args=([ahk_interpreter, ahk_script],)).start()  # 启动一个线程运行.ahk文件

Thread(target=subprocess.run, args=([exe_file],)).start()  # 启动一个线程运行.exe文件
