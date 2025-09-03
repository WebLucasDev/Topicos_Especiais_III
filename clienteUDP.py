import socket

HOST = 'localhost'  
PORT = 12345        
TIMEOUT = 5         

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(TIMEOUT)

try:
    mensagem = "Olá, servidor!"
    client_socket.sendto(mensagem.encode('utf-8'), (HOST, PORT))
    data, server_addr = client_socket.recvfrom(1024)
    print(f"Resposta do servidor ({server_addr}): {data.decode('utf-8')}")

except socket.timeout:
    print(f"Nenhuma resposta em {TIMEOUT} segundos. Verifique se o servidor UDP está rodando.")

except Exception as e:
    print(f"Erro no cliente UDP: {e}")

finally:
    client_socket.close()