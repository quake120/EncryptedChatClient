import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [
    Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA,
    Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

HOST = '34.211.148.140'
PORT = 45000
seperator_token = "<SEP>"

s = socket.socket()
s.connect((HOST, PORT))
print("[+] Connected.")

name = input("Enter Name:")

  
def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input("Message: ")

    if to_send.lower() == "q":
        break

    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {name}{seperator_token}{to_send}{Fore.RESET}"

    s.send(to_send.encode())

s.close()
