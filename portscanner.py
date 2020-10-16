
import socket

porta = input('Digite uma porta: ')
porta2 = input('Digite outra porta: ')

x = 0
while(porta <= porta2):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    codigo = cliente.connect_ex(('Aqui voce colocara o ip da maquina que vc deseja escanear', porta))
    if codigo == 0:
        print porta, 'OPEN'

    porta += 1

#codigo = cliente.connect_ex((ip, porta))

#print codigo
