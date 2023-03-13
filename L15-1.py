import socket
import logging

# задаємо адресу сервера та порт
HOST = 'localhost'
PORT = 5000

# налаштування системи логування
logging.basicConfig(filename='chat_server.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# створюємо сокет і прив'язуємо його до заданої адреси
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# починаємо слухати порт
server_socket.listen()

logging.info(f'Server started on {HOST}:{PORT}')

while True:
    # приймаємо з'єднання
    client_socket, client_address = server_socket.accept()
    logging.info(f'Connected by {client_address}')

    try:
        # надсилаємо повідомлення клієнту
        client_socket.sendall(b'Hello from server')

        # отримуємо повідомлення від клієнта
        data = client_socket.recv(1024)
        logging.info(f'Received: {data.decode()}')

    except Exception as e:
        logging.error(f'Error: {e}')

    try:
        client_socket, client_address = server_socket.accept()
        logging.info(f'Connected by {client_address}')

    except Exception as e:
        logging.warning(f'Failed to connect to client: {e}')

    finally:
        # закриваємо з'єднання
        client_socket.close()
        logging.warning(f'Connection with {client_address} closed')


server_socket.close()
