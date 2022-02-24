[Setup]
AppName=CPPM 0.x Beta
AppVersion=0.1
DefaultDirName={autopf}\Tyler887/CPPM
DefaultGroupName=Cross-Platform Package Manager
PrivilegesRequiredOverridesAllowed=commandline dialog
[Files]
Source: ".\dist\cppm.exe"; DestDir: "{app}"
[Run]
Filename: "{app}\cppm.exe"; Description: "Open CPPM shell"
Filename: "https://github.com/Tyler887/CPPM"; Description: "Open CPPM GitHub repository"
