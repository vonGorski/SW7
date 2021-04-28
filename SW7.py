import socket
# to zawsze tak
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket
# Create a new socket using the given address family,
#  socket type and protocol number. 
#  The address family should be AF_INET (the default),
#   AF_INET6, AF_UNIX, AF_CAN, AF_PACKET, or AF_RDS. 
#   The socket type should be SOCK_STREAM (the default)
ADRES = 'www.weka.pwr.edu.pl'
REQUEST = 'GET / HTTP/1.1\r\nHost:' + ADRES + '\r\n\r\n'
# zawsze 80, pierwszy parametr moze byc zmienna bo jest to adres
SOCKET.connect((ADRES, 80))
# host is a string representing either a hostname 
# in Internet domain notation
# port is an integer.
# wymaga encode pozniewaz musi byc w formie bitowej
SOCKET.send(REQUEST.encode())
# Send data to the socket. 
# The socket must be connected to a remote socket.
BUFSIZE= 1024
RESPONSE = SOCKET.recv(BUFSIZE)
# The return value is a bytes object 
# representing the data received.
FILE = open("odczyt.txt", "w")
FILE.write(RESPONSE.decode())
FILE.close()
print(RESPONSE.decode())
SOCKET.close()