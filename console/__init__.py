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

def checkisexit():
    try:
        getpass.getpass("Enter to continue, Ctrl+C to exit\n")
    except:
        print("Exiting...")
        raise SystemExit
    
def execute(command: str):
    splitted = command.split(" ")
    if len(splitted) > 1:
        eval(f"commands.{splitted[0]}({str(splitted[1:]).replace("[", "").replace("]", "")})")
    else:
        eval(f"commands.{splitted[0]}()")