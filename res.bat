python get_message.py
set err=%ERRORLEVEL%
echo 'Packing up. May restart. Use CTL+C to close'
timeout 10
if %err% GEQ 1 res.bat