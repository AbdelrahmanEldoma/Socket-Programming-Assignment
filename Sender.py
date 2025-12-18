import socket
HOST = '127.0.0.1'
PORT = 5000

def parity_bit(data):
    ones = sum(bin(ord(c)).count('1') for c in data)
    return str(ones % 2)

text = input("Enter text: ")
method = "PARITY"
control = parity_bit(text)
packet = f"{text}|{method}|{control}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet.encode())