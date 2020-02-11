import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Riona, the IP is either')
print('68.148.17.19')
print('OR 10.0.0.105')

#host = '10.0.0.105'
host = input('Host IP = ')
#name = testman
name = input('Name = ')
port = 6969
e = 'utf-8'
s.connect((host,port))
print("Connected to "+ host +"!")
s.send(bytes(name,e))
print('')
while True:
	data = input('')
	s.send(bytes(data,e))
	reply = s.recv(64)
	print(reply.decode(e))

s.close()
print (reply.decode(e))