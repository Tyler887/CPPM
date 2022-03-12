from os.path import expanduser
home = expanduser("~")
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
  print("Importing glob module...")
  import glob
  print("Importing art, requests and colorama modules...")
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
  try:
    import requests
  except ImportError:
    print("Package requests not installed. Executing pip to request install...")
    os.system("python -m pip install requests")
    print("Attempting import again...")
    import requests
  os.system('cls' if os.name=="nt" else 'clear') # else coloring will obviously not work on windows console host
  print(f"{Back.WHITE}{Fore.BLACK}Welcome to CPPM!{Style.RESET_ALL}")
  time.sleep(0.5)
  print("Launching CPPM...")
except KeyboardInterrupt:
  print(f"You are entering the system command line shell, `{app}'. This is only for advanced users!\nType HELP for a list of commands. If you did not mean to go here, type EXIT.")
  os.system(app)
  os.system("python " + __file__)
  exit()
print("Type `help' or `?' for command list, type `license' for legal notices")
if not os.path.isdir(f"{home}/cppm-{os.name}"):
  print("Setting up. Please wait.")
  os.makedirs(f"{home}/cppm-{os.name}")
  os.makedirs(f"{home}/cppm-{os.name}/apps")
  infofile = open(f"{home}/cppm-{os.name}/info.txt", 'a+')  # open file in append mode
  infofile.write('This folder describes the files for CPPM.')
  infofile.close()
while True:
  try:
    cmd = input("cppm>")
    if cmd == "help" or cmd == "?":
      print("install: Install package from the internet")
      print("uninstall: Uninstall package")
      print("upgrade: Upgrade package from the internet")
      print("help: Open this help page")
      print("?: alias of help")
      print("exit: Exit CPPM and stop it's processes")
      print("list: List the packages installed (usally stored in a text file)")
    elif cmd == "list":
      with open(os.path.dirname(os.path.realpath(__file__)) + '/pkglist.txt', 'r') as reader:
        print(reader.read())
    elif cmd == "install":
      print("Usage: install <GitHub repository>\n\nHelps install a package through a GitHub Release. This is so\nCPPM can reject closed-source apps like the old PowerShell (or 'Windows PowerShell').\n\nFor example, to install PowerShell Core (open-source version of Windows PowerShell), run:\n          install PowerShell/PowerShell")
    elif cmd == "exit":
      exit()
    else:
      if cmd != "" and not cmd.startswith("install ") and not cmd.startswith("upgrade ") and not cmd.startswith("uninstall "):
         print(f"{Fore.RED}Invalid CPPM command `{cmd}'!{Style.RESET_ALL} Type `help' or `?' for a list of commands that\ncan be executed in CPPM.")
      if cmd.startswith("install "):
          asset = input("Provide the asset: ")
          repo = cmd.replace("install ","",1)
          
          os.makedirs(f"{home}/cppm-{os.name}/apps/{repo}")
          print("Attempting to get latest GitHub release...")
          link = f"https://github.com/{repo}/releases/latest/download/{asset}"
          file_name = f"{home}/cppm-{os.name}/apps/{repo}/{asset}"
          with open(file_name, "wb") as f:
             print("Downloading %s" % asset)
             response = requests.get(link, stream=True)
             total_length = response.headers.get('content-length')
          
             if total_length is None: # no content length header
               f.write(response.content)
             else:
               dl = 0
               total_length = int(total_length)
               for data in response.iter_content(chunk_size=4096):
                  dl += len(data)
                  f.write(data)
                  done = int(50 * dl / total_length)
                  per = int(done * 2)
                  import os

                  if os.path.exists(f"{dir}/{asset}") and os.path.getsize(f"{dir}/{asset}") > 25:
                       sizedisplay = 1
                       size = os.path.getsize(f"{dir}/{asset}")
                  else:
                       sizedisplay = 0
                  if sizedisplay:
                    sys.stdout.write("\r%s%s" % ('■' * done, ' ' * (50-done)) + f" | {per}% Done ({size} Bytes)" )
                  else:
                    sys.stdout.write("\r%s%s" % ('■' * done, ' ' * (50-done)) + f" | {per}% Done" )    
                  sys.stdout.flush()
          print("!")
          if asset.endswith(".zip"):
             print(f"Extracting {asset}...")
             import zipfile
             with zipfile.ZipFile(f"{home}/cppm-{os.name}/apps/{repo}/{asset}", 'r') as zip_ref:
                zip_ref.extractall(f"{home}/cppm-{os.name}/apps/{repo}")
             os.unlink(f"{home}/cppm-{os.name}/apps/{repo}/{asset}")
          print(f"Remember to add this package to the PATH using this PowerShell command:\n$env:Path += '{home}/cppm-{os.name}/apps/{repo}'")
  except KeyboardInterrupt:
       print("^C")
