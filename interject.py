from string import Template
from pathlib import Path

p = Path("interject.txt").absolute()

interject = Template(p.read_text())

linux = input("Linux \n> ").capitalize()
gnu = input("GNU \n> ").capitalize()
corelibs = input("made useful by the... 1 \n> ")
shell_utilities = input("made useful by the... 2 \n> ")
system_components = input("made useful by the... 3 \n> ")
os = input("...comprising a... \n> ")
posix = input("as defined by... \n> ")
kernel = input("kernel \n> ")

adlib = interject.substitute(linux=linux, 
                             gnu=gnu, 
                             corelibs=corelibs, 
                             shell_utilities=shell_utilities, 
                             system_components=system_components, 
                             os=os, 
                             posix=posix, 
                             kernel=kernel)

print(adlib)
