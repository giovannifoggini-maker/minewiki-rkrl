@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Avvio del server locale (porta iniziale 10000, poi la successiva libera)...
py avvia_localhost.py
if errorlevel 1 (
  echo.
  echo Non e' stato possibile avviare Python. Verifica di avere Python installato e il comando "py" disponibile.
  pause
)
