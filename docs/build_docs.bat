@echo off
echo Building robosapiensIO Documentation...
cd /d "c:\Users\dell\Documents\rpio\docs"
C:\Users\dell\Documents\rpio\.venv\Scripts\sphinx-build.exe -b html . _build\html
echo.
echo Documentation built successfully!
echo Opening in browser...
start "" "_build\html\index.html"
pause
