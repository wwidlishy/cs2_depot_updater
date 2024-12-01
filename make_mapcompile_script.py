base = \
"""@echo off
set CS2install=Counter-Strike Global Offensive
set ProjectName=$PNAME
set MapName=$MNAME
"%CS2install%\\game\\bin\\win64\\resourcecompiler.exe" -threads 5 -fshallow -maxtextureres 256 -dxlevel 110 -quiet -unbufferedio -i "%CS2install%/content/csgo_addons/%ProjectName%/maps/%MapName%.vmap"  -noassert  -world -bakelighting -lightmapMaxResolution 1024 -lightmapDoWeld -lightmapVRadQuality 1 -lightmapLocalCompile -phys -vis -nav -retail -breakpad -nop4 -outroot "%AppData%\\..\\Local\\Temp\\valve\\hammermapbuild\\game" -lightmapcpu
xcopy "%AppData%\\..\\Local\\Temp\\valve\\hammermapbuild\\game\\csgo_addons\\%ProjectName%\\maps\\%MapName%.vpk" "%CS2install%\\game\\csgo_addons\\%ProjectName%\\maps\\" /y
pause"""

print("Do not move the bat file created!")

pname = input("Project name: ")
mname = input("Map file name: ")

with open(f"Compile {mname} in {pname}.bat", "w") as w:
    w.write(base.replace("$MNAME", mname).replace("$PNAME", pname))

print(f"Script made: Compile {mname} in {pname}.bat")
