import socket, os
def hello():
    print("Hello, OpenConsole Users!")
def sum(a, b):
    try:
        print(int(a)+int(b))
    except:
        print("Not Numbers!")
        print("Invalid use of sum command")
def ip():
    print("Node:", socket.gethostname())
    print("IP:  ", socket.gethostbyname(socket.getfqdn()))
def echo(msg):
    print(msg)
def cd(dir):
    try:
        os.chdir(dir)
    except:
        print("Invalid directory")
def dir():
    print(os.getcwd())
def cls():
    os.system("cls")
clear = cls