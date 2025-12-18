import socket, random
HOST = '127.0.0.1'
PORT1 = 5000
PORT2 = 6000

#run the corruptor first then the receiver then the sender
#corruptining the data using Character Substitution

def corrupt(data):
    i = random.randint(0, len(data)-1)
    return data[:i] + chr(random.randint(65,90)) + data[i+1:]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT1))
    s.listen()
    conn, _ = s.accept()
    packet = conn.recv(1024).decode()

    data, method, ctrl = packet.split('|')
    data = corrupt(data)
    new_packet = f"{data}|{method}|{ctrl}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.connect((HOST, PORT2))
        s2.sendall(new_packet.encode())