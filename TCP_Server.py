#server
import socket
import json
import time
import operator
import platform
import struct
import TCP_base

address = ('localhost', 9102)

# AF_INET = ipv4;  SOCK_STREAM:TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
s.bind(address)

s.listen(5)


def send_start(conn):

    conn.send(bytes('test hi'))


while True:
    print('----server wait')
    conn, addr = s.accept()

    ## send start train
    # send_start(conn)

    data_head = TCP_base.parse_head(conn)
    data_len = data_head['data_len']
    data = conn.recv(data_len)
    print('--data----------', data)

    # print(data_head)

    time.sleep(5)

    head_len, head_bytes = TCP_base.build_header('this is tet', data)
    conn.send(head_len)
    conn.send(head_bytes)

    if operator.__eq__(TCP_base.cmd_pk_model, data_head):
        conn.sendall('pk finish, new is bad'.encode('utf-8'))
    else:
        conn.sendall('pk finish, not eq '.encode('utf-8'))
    conn.close()

# s.close()
