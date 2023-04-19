import subprocess
subprocess.Popen(["python3", "discussion/manage.py",  "runserver",  "8001"])
subprocess.call(["python3", "CSE_site/manage.py",  "runserver",  "8000"])