import random
import os
import json
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

global encKey
global keySet

encKey = bytes
keySet = False


def generateKey(filename):
    key = os.urandom(32)
    keyData = bytearray(key)
    w = open(filename, 'wb')
    w.write(keyData)


def encrypt(msg):
    iv = os.urandom(16)
    global encKey
    aes = AES.new(encKey, AES.MODE_CFB, iv)
    encodedMsg = aes.encrypt(msg)
    msgBlock = {
        "msg": b64encode(encodedMsg).decode(),
        "iv": b64encode(iv).decode()
    }
    msgToSend = json.dumps(msgBlock)
    print(msgToSend)


def decrypt(msgBlock):
    global encKey
    msgBlockParsed = json.loads(msgBlock)
    aes = AES.new(encKey, AES.MODE_CFB, b64decode(msgBlockParsed['iv']))
    decryptedMsg = aes.decrypt(b64decode(msgBlockParsed['msg']))
    print(decryptedMsg)


def loadKey():
    fileName = input("Enter key filename: ")
    kFile = open(fileName, 'rb')
    global encKey
    global keySet
    encKey = bytes(kFile.read())
    keySet = True
    print("Loaded key ..." + str(len(encKey)))
    menu()


def menu():
    opt = input(
        "Choose Option:\n1) New Key 2) Load Key 3) Encrypt String 4) Decrypt String\n> "
    )

    if (opt == '1'):
        name = input("Enter filename: ")
        generateKey(name)
        menu()
    if (opt == '2'):
        loadKey()
    if (opt == '3'):
        if (keySet == False):
            print("No key has been set! Please load first")
            menu()
        msg = input("Enter message to encrypt: ")
        encrypt(msg)
        menu()
    if (opt == '4'):
        if (keySet == False):
            print("No key has been set! Please load a key first")
            menu()
        encoded = input("Enter encoded bytes: ")
        decrypt(encoded)
        menu()


menu()
