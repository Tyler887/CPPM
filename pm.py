print("Importing os module...")
import os
print("Importing sys module...")
import sys
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
  os.system("python -m pip install art")
  print("Attempting import again...")
  from colorama import *
print("Launching pm...")
os.system('cls' if os.name=="nt" else 'clear')
tprint("Hello World!")
print(f"{Fore.CYAN}Welcome to PM{Style.RESET_ALL}. Type `help' or `?' for command list, type `license' for legal notices")
while True:
  cmd = input("pm>")
  if cmd == "help" or cmd == "?":
    print("install: Install package from the internet")
    print("uninstall: Uninstall package")
    print("upgrade: Upgrade package from the internet")
    print("help: Open this help page")
    print("?: alias of help")
    print("exit: Exit PM and stop it's processes")
    print("list: List the packages installed (usally stored in a text file)")
  elif cmd == "list":
    with open(os.path.dirname(os.path.realpath(__file__)) + '/pkglist.txt', 'r') as reader:
      print(reader.read())
