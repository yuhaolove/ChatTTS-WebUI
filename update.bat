@echo off

REM 设置Python路径
set "PATH=%cd%\environment\Scripts;%cd%\environment\Library\bin;%cd%\environment;%PATH%"

REM 检查并更新ChatTTS
echo Checking and updating ChatTTS...
python update_chattts.py

REM 提示更新完成
echo Update complete!
pause
