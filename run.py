import os
n = 1
def banner():
        print  ("""\033[94m
████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        \033[91mVersion - dev-1.1 coded by ShuBhamg0sai""")

while n>0:
    banner()
    print("CTRL + z for exit")
    cou = eval(input("\033[1;32m Enter your country code\033[1;34m:\033[1;31m➤"))
    num = eval(input("\033[1;32m Enter your number \033[1;34m:\033[1;31m➤"))
    os.system("python3 tracker.py"+" "+cou+num)

