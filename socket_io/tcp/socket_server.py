import socket

s = socket.socket()  #创建socket对象
host = socket.gethostname()  #获取本机主机名
port = 12345
s.bind((host, port))         #绑定端口

s.listen(5)    #监听，等待客户端连接
while  True:
	c, addr = s.accept()  #建立客户端连接
	print('连接地址', addr)
	c.send(bytes("欢迎访问菜鸟教程！", encoding="utf-8"))
	c.close()   #关闭连接