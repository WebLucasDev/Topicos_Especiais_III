import socket

HOST = 'localhost' 
PORT = 12345       
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    
    mensagem = "Olá, servidor!"
    client_socket.sendall(mensagem.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"Resposta do servidor: {data.decode('utf-8')}")

except ConnectionRefusedError:
    print(f"Não foi possível conectar em {HOST}:{PORT} -- verifique se o servidor está rodando.")
except Exception as e:
    print(f"Erro no cliente TCP: {e}")
finally:
    client_socket.close()