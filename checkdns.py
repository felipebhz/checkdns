# coding=utf8

# 31.220.16.242
# 216.58.222.46


import socket
import time
import webbrowser

def checkdns():
        print time.ctime()
        retorno = True
        try:
            ip = socket.gethostbyname('google.com') #Domain name to be tested for DNS propagation
            print ("Checked Host's IP is: " + ip)
            if ip == "***.***.***.***": #Target's server IP Address. Known as "new server".
                retorno = False
                url = 'http://www.google.com/' #URL to open if DNS propagation is done, at least in your ISP
                webbrowser.open_new_tab(url)
            else:
                print "DNS not propagated yet. Waiting 15 minutes."
        except socket.gaierror:
            print "No hostname defined for the domain name. Waiting 15 minutes."
        return retorno

condicao = True
while condicao:
    condicao = checkdns()
    time.sleep( 900 )
