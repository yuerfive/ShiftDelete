; 拦截 Shift + Delete 快捷键
+Delete::
    ; 获取当前选中的文件路径
    FilePath := GetSelectedFilePath()
    if (FilePath) {
        ; 调用 Python 脚本处理文件删除
        Run, %A_WorkingDir%\MoveFile.exe "%FilePath%"
    }
return

; 获取当前选中的文件路径
GetSelectedFilePath() {
    Clipboard := ""  ; 清空剪贴板
    Send, ^c  ; 模拟 Ctrl + C 复制选中的文件路径
    ClipWait, 1  ; 等待剪贴板内容
    if (ErrorLevel) {
        MsgBox, 无法获取选中的文件路径
        return
    }
    FilePath := Clipboard
    Clipboard := ""  ; 清空剪贴板
    return FilePath
}
