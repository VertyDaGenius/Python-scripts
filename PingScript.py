# this is my first time coding in python so please do not judge this

import subprocess
import time
ip_address = input('Type an IP address to ping!')

while True:
    ping_command = f"ping {ip_address}"

    output = subprocess.run(ping_command, capture_output=True)

    if output.returncode == 0:
        print(f"{ip_address} Is Up.")
    else:
        print(f"{ip_address} Is Down.")
    time.sleep(1)
