import socket
import os
import os.path
import urllib.request
print("############################################")
print("# I Wish You Like it                       #")
print("# Simple & online Md5 HashCracker          #")
print("#    I wrote These Codes just in 15m       #")
print("#    Contact Me:mostafa-zarei@hotmail.com  #")
print("############################################\n\n")

while 1 :

    path = (os.getcwd())
    flpath = path+'\Cracked Hashes'

    if not os.path.exists(flpath): os.makedirs(flpath)

    Staticurl = "http://md5cracker.com/qkhash.php?option=plaintext&pass="
    Hash = input("Enter The Md5 Hash Here = ")
    Url = Staticurl+Hash
    name = Hash

    urllib.request.urlretrieve(Url , '1.txt')
    Outfile = open('1.txt','r+')
    for line in Outfile :
            print(line ,file=Outfile, end=' ')
            Outfile = open(path+"/Cracked Hashes/%s.txt" % name , 'w+')
            print(line , end='')

    print("The Cracked Hash Saved in Cracked Hashes 'Folder' Also! \n")
    s = input("Press Any key to continue")
























