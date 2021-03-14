import os
import subprocess

def server_list():
    server_list = subprocess.check_output(['msm', 'server', 'list']).decode('utf-8')
    return str(server_list)
