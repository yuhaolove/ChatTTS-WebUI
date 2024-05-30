@echo off

REM 设置环境变量
echo Setting up environment variables...
set "PATH=%cd%\environment\Scripts;%cd%\environment\Library\bin;%cd%\environment;%PATH%"

REM 运行webui下的main.py
echo Running web UI...
python webui\main.py


pause

