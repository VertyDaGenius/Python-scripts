# requirements:
# colorama

import subprocess
import time
import colorama
from colorama import Fore

ip_address = input('Type an IP address to ping!')

while True:
    ping_command = f"ping {ip_address}"

    output = subprocess.run(ping_command, capture_output=True)

    if output.returncode == 0:
        print(Fore.GREEN + ip_address + " Is Up.")

    else:
        print(Fore.RED + ip_address + " Is Down/invalid.")
    time.sleep(1)
