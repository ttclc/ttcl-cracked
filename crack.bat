@echo off
python pyinsxtractor.py %1
echo.
python patcher.py %1_extracted\ttClient1.4.pyc cracked_ttcl.pyc
echo.
echo.
if %errorlevel% == 0 (
echo Operation successful. You can launch cracked pyc file via Python.
)
pause > NUL
