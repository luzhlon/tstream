
import socket   #socket模块
import codecs
import time

HOST = '127.0.0.1'
PORT = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT)); s.listen(5)
while 1:
    conn,addr = s.accept()   #接受TCP连接，并返回新的套接字与IP地址
    print('Connected by',addr)
    while 1:
        try:
            conn.send("abcdefg\n".encode())
            time.sleep(3)
            # data = conn.recv(1024)
            # if not data: break
            # data = codecs.encode(data.decode(), 'rot13')
            # conn.send(data.encode())
        except ConnectionResetError:
            break
    conn.close()     #关闭连接
