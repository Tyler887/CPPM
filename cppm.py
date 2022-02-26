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
    elif cmd == "exit":
      exit()
    else:
      if cmd != "" and not cmd.startswith("install ") and not cmd.startswith("upgrade ") and not cmd.startswith("uninstall "):
         print(f"{Fore.RED}Invalid CPPM command `{cmd}'!{Style.RESET_ALL} Type `help' or `?' for a list of commands that\ncan be executed in CPPM.")
      if cmd.startswith("install "):
          asset = input("Provide the asset: ")
          repo = cmd.replace("install ","",1)
          print("Attempting to get latest GitHub release...")
          response = requests.get("https://api.github.com/repos/" + repo + "/releases/latest")
          file_name = "~/cppm/" + asset
          with open(file_name, "wb") as f:
             print("Downloading %s" % file_name)
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
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
            sys.stdout.flush()
  except KeyboardInterrupt:
       print("\nNote: Ctrl+C restarts CPPM! It does not kill the process.")
       os.system("python " + __file__)
       exit()
