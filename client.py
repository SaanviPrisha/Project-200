import socket
from threading import Thread

nickname = input("Choose your nickname: ")

#create a TCP socket called client-ip add. +port
#socket.socket(family,socket type) by default ipv4-AF_INET
#sock_stream- tcp socket...  sock_dgram=> udp socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
#port can be any number.just make sure it is not anything lower than 1024
port = 7000

client.connect((ip_address, port))

print("Connected with the server...")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()
