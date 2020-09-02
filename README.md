# wrldc_mis_flask_ui

This the Dashboard Web app for MIS software at WRLDC

# Setup instructions
* run setup_env.bat file to setup virtual environment
* download nssm from https://nssm.cc/download
* In the 'Path' system environment variable, add the path of nssm.exe, so that nssm.exe can be recognized in command line
* run setup_service.bat file to run the flask server as a background service
* Optionally use run_server.bat, if we desire to run the server via command line

### using nssm.exe to create python flask server as a background service in windows
* https://www.techcoil.com/blog/how-to-use-nssm-to-run-a-python-3-application-as-a-windows-service-in-its-own-python-3-virtual-environment/
* https://nssm.cc/usage

### create a windows service by name mis_dashboard
```bat
nssm.exe install mis_dashboard "path\to\run_server.bat"
```

### editing a windows service by name mis_dashboard via nssm GUI
```bat
nssm.exe edit mis_dashboard
```

### Setup output stream files for service name mis_dashboard
````bat
nssm.exe set mis_dashboard AppStdout "path\to\app_output.log"
nssm.exe set mis_dashboard AppStderr "path\to\app_output.log"
```

### start/delete/pause/stop a service in windows
```bat
sc start svc_name
sc delete svc_name
sc pause svc_name
sc stop svc_name
```

### see a service info in windows
````sc query svc_name```

### run flask app as a windows service without nssm using pywin32
* Run flask app as a windows service using pywin32 module - https://stackoverflow.com/questions/23550067/deploy-flask-app-as-windows-service

* Run flask app pyinstaller exe file as a windows service - https://stackoverflow.com/questions/55677165/python-flask-as-windows-service

### run an infinite loop as a service using pywin32
* http://ryrobes.com/python/running-python-scripts-as-a-windows-service/