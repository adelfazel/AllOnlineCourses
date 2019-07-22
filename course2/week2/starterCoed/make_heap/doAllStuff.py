import os
import subprocess
subprocess.call(['python3','createTest.py'],shell=True)
print("testCreated")
subprocess.call(['cat','testname','|','python3','naive.py','>>','naive.txt'],shell=True)
