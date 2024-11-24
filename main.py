import requests
import time
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def show_banner():
    print(f'''{Fore.RED}
 
  ▄████  ▄▄▄       ██▓    ▄▄▄      ▒██   ██▒▓██   ██▓
 ██▒ ▀█▒▒████▄    ▓██▒   ▒████▄    ▒▒ █ █ ▒░ ▒██  ██▒
▒██░▄▄▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ░░  █   ░  ▒██ ██░
░▓█  ██▓░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██  ░ █ █ ▒   ░ ▐██▓░
░▒▓███▀▒ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒ ▒██▒  ░ ██▒▓░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░▒▒ ░ ░▓ ░   ██▒▒▒ 
  ░   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░░   ░▒ ░ ▓██ ░▒░ 
░ ░   ░   ░   ▒     ░ ░    ░   ▒    ░    ░   ▒ ▒ ░░  
      ░       ░  ░    ░  ░     ░  ░ ░    ░   ░ ░     
                                             ░ ░     
''')


def send_message(webhook_url, message):
    username = "Galaxy Spam Tool"
    data = {
        "content": f"@everyone {message}",
        "username": username,
        "tts": True
    }

    headers = {
        "content-type": "application/json"
    }

    try:
        response = requests.post(webhook_url, json=data, headers=headers)

        if response.ok:
            print(f"{Fore.GREEN}[+] Mensaje enviado con éxito al webhook: {webhook_url}")
            return True
        elif response.status_code == 429:
            print(f"{Fore.RED}Error 429, demasiadas solicitudes. Reintentando en 30 segundos...")
            time.sleep(30)
        else:
            print(f"{Fore.RED}Error al enviar mensaje: {response.status_code} - {response.reason}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error de conexión: {e}")

    return False


def spam_single_webhook():
    webhook_url = input(f"{Fore.GREEN}Ingresa el webhook al que deseas enviar el mensaje: ")
    message = input(f"{Fore.GREEN}Pon el mensaje que quieres spamear aquí: ")

    print(f"{Fore.GREEN}[+] El spam ha comenzado, presiona CTRL + C para detenerlo")
    time.sleep(1)

    attempt_count = 0
    sent_count = 0

    try:
        while True:
            if send_message(webhook_url, message):
                sent_count += 1
            attempt_count += 1
    except KeyboardInterrupt:
        print(f"{Fore.GREEN}Spam detenido. Mensajes enviados: {sent_count}, Intentos totales: {attempt_count}")


def spam_multiple_webhooks():
    try:
        with open("webhooks.txt", "r") as file:
            webhooks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}El archivo 'webhooks.txt' no fue encontrado.")
        return

    if not webhooks:
        print(f"{Fore.RED}No se encontraron webhooks en el archivo 'webhooks.txt'.")
        return

    message = input(f"{Fore.GREEN}Pon el mensaje que quieres spamear aquí: ")

    print(f"{Fore.GREEN}[+] El spam ha comenzado, presiona CTRL + C para detenerlo")
    time.sleep(1)

    attempt_count = 0
    sent_count = 0
    failed_previous = False

    try:
        while True:
            for webhook_url in webhooks:
                if send_message(webhook_url, message):
                    sent_count += 1
                    failed_previous = False
                else:
                    if failed_previous:
                        print(f"{Fore.RED}30 segundos para volver a enviar el spam")
                        time.sleep(30)
                    else:
                        time.sleep(1)
                    failed_previous = True
            attempt_count += 1
    except KeyboardInterrupt:
        print(f"{Fore.GREEN}Spam detenido. Mensajes enviados: {sent_count}, Intentos totales: {attempt_count}")

def main():
    show_banner()
    print(f"{Fore.YELLOW}Selecciona una opción:")
    print(f"{Fore.CYAN}1. Enviar spam a un solo webhook ingresado manualmente.")
    print(f"{Fore.CYAN}2. Enviar spam a múltiples webhooks desde el archivo 'webhooks.txt'.")
    
    try:
        option = int(input(f"{Fore.GREEN}Ingresa tu elección (1 o 2): "))
        if option == 1:
            spam_single_webhook()
        elif option == 2:
            spam_multiple_webhooks()
        else:
            print(f"{Fore.RED}Opción no válida. Saliendo...")
    except ValueError:
        print(f"{Fore.RED}Entrada inválida. Saliendo...")

if __name__ == "__main__":
    main()
