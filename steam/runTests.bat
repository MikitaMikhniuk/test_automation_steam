@echo off
python3 --version > NUL 2>&1
if ERRORLEVEL 1 echo "No Python3 distributable! PLease isntall Python3 to proceed." & exit 1

pip install --upgrade pip
python3 -m venv steam_env
steam_env\Scripts\pip install pytest
steam_env\Scripts\pip install selenium
steam_env\Scripts\pip install webdriver_manager
steam_env\Scripts\pip install pytest-html
steam_env\Scripts\pip install pytest-repeat  
steam_env\Scripts\python -m pytest --html=results.html --self-contained-html