import console
from console.commands import *
from console import color
from console import commands
console.clear()

print(color.Fore.MAGENTA+r"""
 _____                    _____                       _      
|  _  |                  /  __ \                     | |     
| | | |_ __   ___ _ __   | /  \/ ___  _ __  ___  ___ | | ___ 
| | | | '_ \ / _ \ '_ \  | |    / _ \| '_ \/ __|/ _ \| |/ _ \
\ \_/ / |_) |  __/ | | | | \__/\ (_) | | | \__ \ (_) | |  __/
 \___/| .__/ \___|_| |_|  \____/\___/|_| |_|___/\___/|_|\___|
      | |                                                    
      |_|                                                    """)
print(color.Fore.MAGENTA+f"Hello, {console.user()}")
console.checkisexit()
while 1:
    inp = input(f"{color.Fore.GREEN}{console.computer()}_{console.user()}{color.Style.RESET_ALL}-$ ")
    try:
        console.execute(inp)    
    except:
        print("Command not found or missing argument")