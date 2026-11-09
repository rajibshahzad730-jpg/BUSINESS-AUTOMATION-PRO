@echo off
REM Builds a single-file Windows executable: dist\BusinessAutomationPro.exe
python -m pip install -r requirements-dev.txt
python -m app.sample_generator
pyinstaller --noconfirm --onefile --windowed --name BusinessAutomationPro ^
  --add-data "sample_data;sample_data" main.py
echo.
echo Done. Your app is in the dist folder.
pause
