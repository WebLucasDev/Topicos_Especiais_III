import socket
import threading

HOST = 'localhost'
PORT = 12345

def manipula_cliente(conn, addr):
    """
    Função executada em uma thread para tratar a conexão com um cliente.
    conn: objeto socket da conexão com o cliente
    addr: tupla (host, porta) do cliente
    """
    try:
        print(f"[{addr}] Conexão estabelecida.")
        data = conn.recv(1024)
        if not data:
            print(f"[{addr}] Cliente desconectou sem enviar dados.")
            return
        mensagem = data.decode('utf-8')
        print(f"[{addr}] Mensagem recebida: {mensagem}")

        resposta = "Mensagem recebida"
        conn.sendall(resposta.encode('utf-8'))

    except Exception as e:
        print(f"[{addr}] Erro ao tratar cliente: {e}")
    
    finally:
        conn.close()
        print(f"[{addr}] Conexão encerrada.")
        
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor TCP aguardando conexões em {HOST}:{PORT}... (CTRL+C para encerrar)")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=manipula_cliente, args=(conn, addr), daemon=True)
            thread.start()

    except KeyboardInterrupt:
        print("\nServidor interrompido manualmente.")

    except Exception as e:
        print(f"Erro no servidor TCP: {e}")
        
    finally:
        server_socket.close()
        print("Servidor TCP encerrado.")

if __name__ == "__main__":
    main()
