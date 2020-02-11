import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Riona, host might be 10.0.0.105')
print('Port is automatically entered (yes it is 6969')


host = input('Host = ')
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