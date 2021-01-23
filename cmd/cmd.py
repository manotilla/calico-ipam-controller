import subprocess
import os

class Calico(object):
    def check_command_exist(self):
        pass
    def get_free_ipam(self):
        data = os.popen("calicoctl ipam show | awk '{print $12}' |tr -d '|'").read()
        return data.strip()