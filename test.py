u = """
import os
import boot
def sbl(t):
    print(f'''
    ===========================================
                   INDASOS VER.9.1
            |=========================|
{t}Mode
login~$User
password~$user''')
sbl("Nomal ")
boot.boot()
while True:
    c = input("INDAS~$")
    boot.cmd(c)
    """

s = u

with open("SBL.py", mode='w') as f:
    f.write(s)
# New file
