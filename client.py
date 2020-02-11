import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('')
print('Riona, host should be 68.148.17.19')
print('')

host = '68.148.17.19'
name = 'Ri'
# host = input('Host IP = ')
#name = input('Name = ')
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
