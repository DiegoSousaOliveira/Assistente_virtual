import socket
from time import sleep

SERVER_IP = "192.168.0.105" # Configure o IP do servidor
PORT = 80

def send_command(command: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(command.encode())
        print(f"Comando enviado: {command}")

if __name__ == "__main__":
    send_command("LED_ON")
    sleep(2)
    send_command("LED_OFF")