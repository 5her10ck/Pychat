# Server program to receive messages. ONE WAY CHAT PROGRAM.

import socket
import sys

s=socket.socket()

host='localhost'
port=1235
msg=''

s.bind((host,port))

s.listen(5)

while True:
    c,a=s.accept()
    print('connected')
    while(msg!='exit'):
        msg=(c.recv(4094)).decode('utf-8')
        print("Client: " + msg)
    print("Client has been disconnected.")
s.close()
sys.exit()
    
  
