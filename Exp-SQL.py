import os
import requests
import sys
import time
import threading
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from colorama import Fore, Style, init

init(autoreset=True)

def blinking_message(message, duration=10):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(Fore.RED + message)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(message) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)

def check_database_errors(ip_address, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            endpoints = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{wordlist_path}' was not found.")
        return

    valid_endpoints = []

    for endpoint in endpoints:
        endpoint = endpoint.strip()
        url = f"http://{ip_address}/{endpoint}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                valid_endpoints.append(url)
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

    if valid_endpoints:
        print("\nFound valid endpoints (200 OK):")
        for valid_url in valid_endpoints:
            print(valid_url)
    else:
        print("No valid endpoints found.")

if __name__ == "__main__":
    print("Welcome to the Database Error Checker!")


    time.sleep(1)

    path_completer = PathCompleter()

    ip_address = input("\nPlease enter the IP address ==>>")

    wordlist_path = prompt("Please enter the path to your wordlist file ==>> ", completer=path_completer).strip()

    animation_thread = threading.Thread(target=blinking_message, args=("HACK Mr : B",), daemon=True)
    animation_thread.start()
    print("\r" + ' ' * 20 + "\r")

    check_database_errors(ip_address, wordlist_path)
