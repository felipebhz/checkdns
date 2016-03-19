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
            ip = socket.gethostbyname('google.com')
            print ("O IP do host verificado é: " + ip)
            if ip == "216.58.22.46":
                retorno = False
                url = 'http://www.google.com.br/'
                webbrowser.open_new_tab(url)
            else:
                print "DNS ainda não atualizado. Aguardando 30s."
        except socket.gaierror:
            print "Nenhum host definido para o domínio. Aguardando 30s."
        return retorno

condicao = True
while condicao:
    condicao = checkdns()
    time.sleep( 30 )