import subprocess
from subprocess import Popen
p = Popen("KillChrome.bat" , shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()
print(p.returncode) # is 0 if success