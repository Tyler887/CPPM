print("Importing os module...")
import os
try:
  app = 'cmd' if os.name=="nt" else 'sh'
  print(f"Loading. Press Ctrl+C to execute {app}.")
  print("Importing sys module...")
  import sys
  print("Importing time module...")
  import time
  print("Importing gnupg module...")
  try:
    import gnupg
  except ImportError:
    print("Package gnupg not installed. Executing pip to request install...")
    os.system("python -m pip install gnupg")
    print("Attempting import again...")
    import gnupg
  print("Importing platform module...")
  import platform
  print("Importing art and colorama modules...")
  try:
    from art import *
  except ImportError:
    print("Package art not installed. Executing pip to request install...")
    os.system("python -m pip install art")
    print("Attempting import again...")
    from art import *
  try:
    from colorama import *
  except ImportError:
    print("Package colorama not installed. Executing pip to request install...")
    os.system("python -m pip install colorama")
    print("Attempting import again...")
    from colorama import *
  os.system('cls' if os.name=="nt" else 'clear') # else coloring will obviously not work on windows console host
  from distutils.core import setup
  import py2exe
except:
    print("An error has occured.")
    exit(1)
setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "cppm.py"}],
    zipfile = None,
)
