import os

a = ["run", "execute", "launch", "play"]
b = ["chrome", "browser"]
c = ["notepad", "editor"]
d = ["player", "media", "wmplayer"]
e = ["sublime"]
f = ["vlc"]
e = ["exit", "bye", "quit"]

while True:
    print("***List of Program:***")
    print("a) Browser")
    print("b) Notepad")
    print("c) Media Player")
    print("d) VLC media player")
    print("e) Sublime text editor")

    print("Please enter your requirement: "  , end='') 

    p = input()

    if (any(ele in p for ele in a) and any(ele in p for ele in c)):
        os.system(c[0])

    elif (any(ele in p for ele in a) and any(ele in p for ele in b)) :
        os.system(b[0])

    elif (any(ele in p for ele in a) and any(ele in p for ele in d)):
        os.system(d[2])
        
    elif (any(ele in p for ele in a) and any(ele in p for ele in e)):
        os.system(e[0] + "_text")

    elif(any(ele in p for ele in a) and any(ele in p for ele in f)):
        os.system(f[0])

    elif (any(ele in p for ele in e)):
        break

    else:
        print("Not Supported")