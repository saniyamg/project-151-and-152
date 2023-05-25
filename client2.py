import socket
from threading import Thread

nickname=input('choose ur nickname')

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000

client.connect((ip_address,port))

print('connected with server')

def receive():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message =='nickname':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('an error occured')
            client.close()
            break

def write():
    while True:
        message ='{}:{}'.format(nickname,input(''))

receive_thread=Thread(target=receive)
receive_thread.start()
write_thread=Thread(target=write)
write_thread.start()
