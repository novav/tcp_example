import struct
import json

cmd_start_model = 'cmd_start_train'
cmd_pk_model = 'cmd_pk_model'

def parse_head(conn):
    head_len = conn.recv(4)  # s1 head-len
    head_len = struct.unpack('i', head_len)[0]
    print('--head-len-', head_len)
    data_head = conn.recv(head_len).decode('utf-8')
    print('--headinfo------', data_head)
    data_head = json.loads(data_head)
    print('--headinfo-json-', data_head)
    return data_head

def build_header(id, data):
    data_len = len(data)
    head_info = {'cmd_id': id, 'data_len': data_len}
    head_json = json.dumps(head_info)
    head_bytes = head_json.encode('utf-8')
    head_bytes_len = len(head_bytes)

    head_len = struct.pack('i', head_bytes_len)

    return head_len, head_bytes

def test_struct():
    a = '您好'
    a = len(a.encode('utf-8'))  # 字节的长度=====这个数据有多大字节
                                #1英文字母 utf-8编码后=1字节
                                #1中文字符 utf-8编码后=3个字节

    a = 48
    print(a)
    # for a in range(200):
    #     ap = struct.pack('i', a)  # struct.pack把数字转换成 固定大小 4个字节的二进制表示形式
    #     print(a, '->', ap)
    a = struct.pack('i', a)
    print(len(a))  # 4个字节
    print(struct.unpack('i', a))  # struct.unpack[0] 把成自己解包会数字
    print(struct.unpack('i', a)[0])  # struct.unpack[0] 把成自己解包会数字

# test_struct()
