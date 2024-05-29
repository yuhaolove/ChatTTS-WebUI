@echo off

REM 设置环境变量
echo Setting up environment variables...
set "PATH=%cd%\environment\Scripts;%cd%\environment\Library\bin;%cd%\environment;%PATH%"

REM 检查并更新ChatTTS
echo Checking and updating ChatTTS...
python update_chattts.py

REM 运行run_webui.bat
call run_webui.bat
