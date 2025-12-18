import socket
HOST = '127.0.0.1'
PORT = 6000

def parity_bit(data):
    ones = sum(bin(ord(c)).count('1') for c in data)
    return str(ones % 2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, _ = s.accept()
    packet = conn.recv(1024).decode()

    data, method, recv_ctrl = packet.split('|')
    comp_ctrl = parity_bit(data)


    print("Received Data :", data)
    print("Method :", method)
    print("Sent Check Bits :", recv_ctrl)
    print("Computed Check Bits :", comp_ctrl)


    if recv_ctrl == comp_ctrl:
        print("Status : DATA CORRECT")
    else:
        print("Status : DATA CORRUPTED")