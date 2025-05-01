import socket
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