import subprocess
subprocess.Popen(["python", "discussion/manage.py",  "runserver",  "8001"])
subprocess.call(["python", "CSE_site/manage.py",  "runserver",  "8000"])