
call nssm.exe install mis_dashboard "%cd%\run_server.bat"
rem call nssm.exe edit mis_dashboard
call nssm.exe set mis_dashboard AppStdout "%cd%\logs\mis_dashboard.log"
call nssm.exe set mis_dashboard AppStderr "%cd%\logs\mis_dashboard.log"
call sc start mis_dashboard