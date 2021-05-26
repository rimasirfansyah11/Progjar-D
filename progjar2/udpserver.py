import socket


SERVER_IP = '192.168.122.90'
SERVER_PORT = 80


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    #buffer size 1024
    print("diterima ", data)
    print("dikirim oleh " , addr)



