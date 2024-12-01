import glob
import subprocess
import shutil
import os

print("Downloading of last nessesary depot requires to be logged into steam")
uname = input("steam user name: ")
password = input("steam password: ")

path = "Counter-Strike Global Offensive"

cmds = [
        f'DepotDownloader.exe DATA'.replace("DATA", i)
        for i in [
            "-app 730 -depot 2347770 -manifest 1473979371368005478",
            "-app 730 -depot 2347771 -manifest 734640093393352243",
            f"-app 730 -depot 2347779 -manifest 3859439092678459074 -username {uname} -password {password}"
        ]
]

print("[...] Downloading (this may take a while)")

for i in cmds:
    os.system(i)

os.system('move "depots/2347770/16559327/game" "Counter-Strike Global Offensive"')
os.system('move "depots/2347770/16559327/content" "Counter-Strike Global Offensive"')
os.system('move "depots/2347771/16559327/game" "Counter-Strike Global Offensive"')
os.system('move "depots/2347771/16559327/content" "Counter-Strike Global Offensive"')
os.system('move "depots/2347770/16559327/content" "Counter-Strike Global Offensive"')
os.system('move "depots/2347770/16559327/game" "Counter-Strike Global Offensive"')

print("Downloaded!\n[...] Patching")

api64_path = path + "\\game\\bin\\win64"
shutil.copy("steam_api64.dll", api64_path)
print("Patched!")
