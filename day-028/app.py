import platform
import os
import sys

print("Process id: ", os.getpid())
print("Parent process id", os.getppid())

print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())

print("Python module lookup path:", sys.path)
print("Command to run Python:", sys.argv)

print("USERNAME environment variable:", os.environ["USERNAME"])

import pathlib
path = pathlib.Path()
print(repr(path))

"""
Exercise 91: Using the glob Pattern to List Files within a Directory
"""

p = pathlib.Path("")
print(p.cwd())
txt_files = p.glob("*.txt")
print("*.txt:", list(txt_files))

import subprocess

result = subprocess.run(["ls"], capture_output=True)
print("stdout: ", result.stdout)
print("stderr: ", result.stderr)


result = subprocess.run( ["ls"], capture_output=True, text=True )
print("stdout: \n", result.stdout)

result = subprocess.run(["ls", "non_existing_file"])
print("rc: ", result.returncode)

code = 'compile("1" + "+1" * 10 ** 6, "string", "exec")'

result = subprocess.run([ sys.executable, "-c", code ])
