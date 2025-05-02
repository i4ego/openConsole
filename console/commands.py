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
def echo(*msg):
    out = str()
    first = True
    for i in msg:
        if first:
            out+=f"{i}"
            first = False
        else:
            out+=f" {i}"
    print(out)
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
def execute(*command):
    cmd = str()
    for i in command:
        cmd+=f" {i}"
    os.system(cmd)
def exit():
    raise SystemExit
def ls(showhidden=False):
    listdir = os.listdir(os.getcwd())
    for i in listdir:
        if i[0] == "." and showhidden=="True":
            print(i)
            continue
        if i[0] != ".":
            print(i)
def read(file):
    content = str()
    try:
        with open(file, "r") as file:
            print(file.read())
    except:
        print("Invalid file!")
def write(file, content):
    try:
        if file not in os.listdir(os.getcwd()):
            raise OSError
        with open(file, "a+") as file:
            file.write("\n"+content)
    except:
        print("Invalid file!")
def help(*anyargs):
    print("""\
All commands:
hello \t\t[no args]
echo \t\t[*message (Any)]
sum \t\t[a, b (Integer)]
ip \t\t[no args]
cls/clear \t[no args]
dir \t\t[no args]
ls \t\t[showhidden (True/False)]
cd \t\t[directory (String)]
read \t\t[filename (String)]
write \t\t[filename, content (String)]
execute \t[command (String)]
help \t\t[no args]
exit \t\t[no args]
""")

if __name__ == "__main__":
    help()