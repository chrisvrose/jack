python messages.py
set err=%ERRORLEVEL%
if %err% GEQ 1 echo 'Packing up. May restart. Use CTL+C to close'
if %err% GEQ 1 timeout 10
if %err% GEQ 1 res.bat
