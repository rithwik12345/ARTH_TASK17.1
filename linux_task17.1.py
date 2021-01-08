import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.1.102",2000))
s.sendto("hello i am LINUX".encode(),("192.168.1.101",2020))
x=s.recvfrom(1024)
y=x[0].decode()
print(x[1][0]+" : "+y)
