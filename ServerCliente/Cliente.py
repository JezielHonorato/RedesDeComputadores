import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.209.1.98", 3001))