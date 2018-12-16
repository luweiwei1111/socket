import socket

s = socket.socket()     #创建socket对象
host = socket.gethostname()  #获取本机主机名
port = 12345

#连接
s.connect((host, port))

 #接收服务端发送过来的数据
recv_buf = str(s.recv(1024),encoding="utf-8")
print(recv_buf)
#关闭连接
s.close()                