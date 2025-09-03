import socket

HOST = 'localhost'
PORT = 12345

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    print(f"Servidor UDP aguardando mensagens em {HOST}:{PORT}... (CTRL+C para encerrar)")

    try:
        while True:
            data, addr = server_socket.recvfrom(1024)
            mensagem = data.decode('utf-8')
            print(f"[{addr}] Mensagem recebida: {mensagem}")

            resposta = "Mensagem recebida"
            server_socket.sendto(resposta.encode('utf-8'), addr)

    except KeyboardInterrupt:
        print("\nServidor UDP interrompido pelo usuário.")

    except Exception as e:
        print(f"Erro no servidor UDP: {e}")
        
    finally:
        server_socket.close()
        print("Servidor UDP encerrado.")

if __name__ == "__main__":
    main()
