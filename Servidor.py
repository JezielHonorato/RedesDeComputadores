import socket;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.209.1.98", 3001))
s.listen(5)
print('aguardando conexâo')

while True:
    clientsocket, adress = s.accept()
    print('conexão de {address} foi estabelecida.')
    
