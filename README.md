# Tópicos Especiais III - Implementações TCP e UDP em Python

Este repositório contém implementações simples de clientes e servidores usando protocolos TCP e UDP em Python. O objetivo é demonstrar as diferenças fundamentais entre os dois protocolos de comunicação em rede.

## Estrutura do Projeto

O projeto consiste em quatro componentes principais:

- **[servidorTCP.py](servidorTCP.py)**: Servidor TCP multi-thread
- **[clienteTCP.py](clienteTCP.py)**: Cliente TCP simples
- **[servidorUDP.py](servidorUDP.py)**: Servidor UDP
- **[clienteUDP.py](clienteUDP.py)**: Cliente UDP com timeout

## Implementação TCP

### Servidor TCP ([servidorTCP.py](servidorTCP.py))

Um servidor TCP que utiliza threads para lidar com múltiplas conexões simultaneamente:

- Usa `socket.SOCK_STREAM` para comunicação TCP
- Implementa tratamento de múltiplos clientes com threads
- Cada conexão é gerenciada em uma thread separada
- Inclui tratamento adequado de exceções e encerramento limpo

### Cliente TCP ([clienteTCP.py](clienteTCP.py))

Um cliente simples que se conecta ao servidor TCP:

- Estabelece conexão com o servidor usando `connect()`
- Envia uma mensagem de texto
- Aguarda e exibe a resposta do servidor
- Implementa tratamento de erros de conexão

## Implementação UDP

### Servidor UDP ([servidorUDP.py](servidorUDP.py))

Um servidor sem conexão que recebe e responde a datagramas:

- Usa `socket.SOCK_DGRAM` para comunicação UDP
- Implementa um loop para receber mensagens de qualquer cliente
- Utiliza `recvfrom()` para obter dados e o endereço do remetente
- Responde diretamente ao endereço de origem

### Cliente UDP ([clienteUDP.py](clienteUDP.py))

Um cliente simples que envia um datagrama e aguarda resposta:

- Envia mensagem usando `sendto()` especificando o endereço de destino
- Implementa timeout para evitar bloqueio indefinido
- Captura e trata erros de comunicação

## Como Executar

### Para comunicação TCP:

1. Inicie o servidor TCP primeiro:
   ```
   python servidorTCP.py
   ```

2. Em um terminal separado, execute o cliente TCP:
   ```
   python clienteTCP.py
   ```

### Para comunicação UDP:

1. Inicie o servidor UDP primeiro:
   ```
   python servidorUDP.py
   ```

2. Em um terminal separado, execute o cliente UDP:
   ```
   python clienteUDP.py
   ```

## Diferenças entre TCP e UDP

Este projeto demonstra as principais diferenças entre os protocolos:

| Característica | TCP | UDP |
|---------------|-----|-----|
| Conexão | Orientado à conexão (`connect`, `accept`) | Sem conexão |
| Confiabilidade | Entrega garantida | Sem garantia de entrega |
| Ordem | Mantém ordem dos pacotes | Sem garantia de ordem |
| API | `sendall/recv` | `sendto/recvfrom` |
| Overhead | Maior (handshake, confirmações) | Menor (sem handshake) |
| Casos de uso | Transferências que exigem confiabilidade | Comunicações rápidas com tolerância a perdas |

## Observações

- As implementações usam `localhost` (127.0.0.1) para comunicação na mesma máquina
- A porta 12345 é usada para ambos os protocolos (em sistemas reais, é recomendável usar portas diferentes)
- Ambas implementações utilizam UTF-8