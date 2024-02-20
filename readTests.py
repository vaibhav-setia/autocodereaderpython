import pytest

# code to read write stuff
# with open("src/__tests__/componentTest.js", "r") as f:
#    contents = f.read()
#    print(contents)
#    with open("test.js", "w") as f:
#       f.write(contents)

import subprocess

# proc = subprocess.Popen('ping google.com', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# tmp = proc.stdout.read()
# print (tmp)
# raw = subprocess.check_output(["npm","test","src/__tests__/componentTest.js"])

from subprocess import run

data = run("npm test test-reader/src/__tests__/componentTest.js", capture_output=True, shell=True, text=True)
print(data.stdout) # If you want you can save it to a variable
print(data.stderr) # ^