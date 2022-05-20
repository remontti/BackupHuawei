#!/usr/bin/python3
from paramiko import SSHClient
import time
import threading
import sys

class OltSSH:
    def __init__(self, ip, authUsername, autPassword,  file_name, difinePort = 22):
        self.client = SSHClient()
        self.f = open(file_name+".txt", "a")
        self.client.load_system_host_keys()
        self.stop = True
        self.client.connect(hostname=ip, username=authUsername, password=autPassword, port=difinePort)
        self.ssh = self.client.invoke_shell()
    def exec(self, comand):
        #print("Iniciando Comando ", comand)
        self.ssh.send(comand+"\n")
        time.sleep(2)
        
    def setStopRead(self,value):
        time.sleep(10)
        self.stop = value
        self.close()
            
           
    def read(self):
        while self.stop:
            try:
                data = self.ssh.recv(1024).decode("utf-8")
                self.f.write(data)
            except:
                continue

                 
    def close(self):
        self.ssh.close()
        self.client.close()
        self.f.close()

        
        
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 6:
        print("Informar 4 args [main.py ip user password port fila_name]")
    else:
        ip = args[0]
        user = args[1]
        password = args[2]
        port = args[3]
        fila_name = args[4]
        model = args[5]
        olt = OltSSH(ip=str(ip), authUsername=user, autPassword=password, file_name=fila_name, difinePort=port )
        r = threading.Thread(target=olt.read, args=())
        r.start()
        if model == "router" :
          comands = ["display current-configuration | no-more"]
        else:
          comands = ["screen-length 0 temporary","display current-configuration"]
        for c in comands:
            olt.exec(c)
        olt.setStopRead(False)
        r.join()
        
