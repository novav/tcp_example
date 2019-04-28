import socket
import json
import struct
import time
import platform
import TCP_base

class Client:
    def __init__(self):
        # self.ip_port = ('127.0.0.1', 9102)
        self.ip_port = ('192.168.220.2', 7000)
        self.utf_8 = 'utf-8'

    def listen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 1 connect
        self.s.connect(self.ip_port)
        # conn, addr = self.s.accept()
        data = self.s.recv(4)  #.decode(self.utf_8)
        print(data)
        # data += b'\x00'
        # print(data)
        print('len==', len(data))
        d = struct.unpack('i', data)
        # data = self.s.recv(4)
        # d = struct.unpack('i', data)
        print('++++++', d)
        # obj.ParseFromString(data)

    def reqire_4(self, cmd, data):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 1 connect
        self.s.connect(self.ip_port)
        # 2 require send data
        # self.s.sendall(cmd.encode(self.utf_8))
        print(cmd)
        data = struct.pack('i', cmd)
        print('send ', data)
        # print(cmd.encode(self.utf_8))
        self.s.send(data)  # send head

        # 3 recv data
        data = self.s.recv(4)  # .decode(self.utf_8)
        print('recv = ', data)
        print('len==', len(data))
        d = struct.unpack('i', data)
        print('--data----------', data)
        # 4 close
        self.s.close()

        return data

    def reqire(self, cmd, data):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 1 connect
        self.s.connect(self.ip_port)
        # 2 require send data
        # self.s.sendall(cmd.encode(self.utf_8))
        head_len, head_info = TCP_base.build_header(cmd, data)
        self.s.send(head_len)   # send head_len 4 Bit
        self.s.send(head_info)  # send head
        self.s.sendall(data.encode(self.utf_8)) #send datas

        # 3 recv data
        # data = self.s.recv(1024).decode(self.utf_8)
        data_head = TCP_base.parse_head(self.s)
        data_len = data_head['data_len']
        data = self.s.recv(data_len)
        print('--data----------', data)
        # print(data)
        # 4 close
        self.s.close()

        return data



def call_ai_server_to_start():
    client = Client()
    client.listen()

    pass


# call_ai_server_to_start()
client = Client()
ss = 3000
out = client.reqire_4(ss, TCP_base.cmd_pk_model)
exit()


def test_call_ai_server_to_compare():

    client = Client()
    ss = 'hilll'
    out = client.reqire(TCP_base.cmd_pk_model, ss)

    print('get from AI-Server---', out)
    return out

def test_listen():
    client = Client()
    client.listen()





