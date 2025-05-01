import console.color
import console.commands
import getpass
import os
import socket

def clear():
    os.system("cls")
def user():
    return getpass.getuser()
def computer():
    return socket.gethostname()

def checkisexit(showkey=True):
    try:
        if showkey:
            getpass.getpass(console.color.Fore.RED+"^C"+console.color.Style.RESET_ALL+"\nEnter to continue, Ctrl+C to exit")
        else:
            getpass.getpass("\nEnter to continue, Ctrl+C to exit")
    except:
        print("\nExiting...")
        raise SystemExit
    
def execute(command: str):
    splitted = command.split(" ")
    if len(splitted) > 1:
        eval(f"commands.{splitted[0]}({str(splitted[1:]).replace("[", "").replace("]", "")})")
    else:
        eval(f"commands.{splitted[0]}()")