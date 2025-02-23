import os
import sys
import time
import platform
import subprocess
import requests
import tarfile
from pathlib import Path
from pystyle import Box
from colorama import Fore, Style, init

init(autoreset=True)

# Tor Expert Bundle download link and folder
TOR_URL = "https://archive.torproject.org/tor-package-archive/torbrowser/14.0.6/tor-expert-bundle-windows-x86_64-14.0.6.tar.gz"
TOR_FOLDER = Path("tor-expert-bundle")
TOR_EXE = TOR_FOLDER / "Tor" / "tor.exe"

def display_banner():
    print(Fore.RED + '''
  _____ _____     _____ _____   ____  ______ ______ _____ _   _  _____ 
 |_   _|  __ \   / ____|  __ \ / __ \|  ____|  ____|_   _| \ | |/ ____|
   | | | |__) | | (___ | |__) | |  | | |__  | |__    | | |  \| | |  __ 
   | | |  ___/   \___ \|  ___/| |  | |  __| |  __|   | | | . ` | | |_ |
  _| |_| |       ____) | |    | |__| | |    | |     _| |_| |\  | |__| |
 |_____|_|      |_____/|_|     \____/|_|    |_|    |_____|_| \_|\_____|
                                                                       
    Automatically Change IP Address and Spoof Your Location
    TG: @Init3xx
''')

# Detect the operating system
def get_os():
    return platform.system().lower()

# Download and extract Tor Expert Bundle for Windows
def setup_tor_windows():
    if not TOR_EXE.exists():
        print(Fore.YELLOW + "[+] Tor not found. Downloading Tor Expert Bundle...")
        try:
            # Download Tor Expert Bundle
            response = requests.get(TOR_URL, stream=True)
            if response.status_code == 200:
                tor_archive = "tor-expert-bundle.tar.gz"
                with open(tor_archive, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(Fore.GREEN + "[+] Download completed. Extracting...")

                # Extract the archive
                with tarfile.open(tor_archive, "r:gz") as tar:
                    tar.extractall(TOR_FOLDER)

                os.remove(tor_archive)
                print(Fore.GREEN + "[+] Tor Expert Bundle extracted successfully.")
            else:
                print(Fore.RED + "[!] Failed to download Tor Expert Bundle.")
                sys.exit(1)
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}")
            sys.exit(1)
    else:
        print(Fore.GREEN + "[+] Tor is already installed.")

# Install Python packages
def install_python_package(package_name):
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'show', package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(Fore.GREEN + f"[+] {package_name} is already installed.")
    except subprocess.CalledProcessError:
        print(Fore.YELLOW + f"[+] {package_name} is not installed. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', package_name], check=True)

# Install system packages (Linux only)
def install_system_package(package_name):
    if get_os() == 'linux':
        try:
            subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(Fore.GREEN + f"[+] {package_name} is already installed.")
        except subprocess.CalledProcessError:
            print(Fore.YELLOW + f"[+] {package_name} is not installed. Installing...")
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', package_name, '-y'], check=True)

# Get current IP via TOR proxy
def get_ip():
    try:
        proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        response = requests.get('https://api.ipify.org', proxies=proxies, timeout=10)
        return response.text
    except requests.exceptions.RequestException:
        return Fore.RED + "[!] Failed to retrieve IP. Check TOR connection."

# Change IP by restarting TOR
def change_ip():
    if get_os() == 'windows':
        tor_command = f'"{TOR_EXE}"'
    else:
        tor_command = 'sudo systemctl reload tor'

    print(Fore.YELLOW + "[+] Reloading TOR to change IP...")
    os.system(tor_command)
    new_ip = get_ip()
    print(Fore.GREEN + f"[+] Your new IP is: {new_ip}")

# Start TOR service
def start_tor():
    if get_os() == 'windows':
        print(Fore.YELLOW + "[+] Starting TOR service on Windows...")
        os.system(f'start "" "{TOR_EXE}"')
    else:
        print(Fore.YELLOW + "[+] Starting TOR service on Linux...")
        os.system('sudo systemctl start tor')
    time.sleep(5)

# Stop TOR service
def stop_tor():
    if get_os() == 'windows':
        print(Fore.YELLOW + "[+] Stopping TOR service on Windows...")
        os.system('taskkill /F /IM tor.exe')
    else:
        print(Fore.YELLOW + "[+] Stopping TOR service on Linux...")
        os.system('sudo systemctl stop tor')

# Main function
def main():
    display_banner()

    # Ensure required packages are installed
    for package in ['pystyle', 'colorama', 'requests']:
        install_python_package(package)

    # Setup TOR based on OS
    if get_os() == 'windows':
        setup_tor_windows()
    elif get_os() == 'linux':
        install_system_package('tor')

    # Start TOR service
    start_tor()

    # Placeholder for future functionality:
    # The 'interface' variable can be used for network-related tasks,
    # such as changing MAC addresses, monitoring traffic, or managing Wi-Fi connections.
    # Currently, this input is not utilized, but it can be integrated into features like:
    # - MAC spoofing for anonymity
    # - Checking network status or reconnecting
    # - Managing multiple network interfaces

    # User input for configuration
    interface = input(Fore.CYAN + "Enter your wireless interface name (e.g., wlan0): ").strip()
    time_interval = int(input(Fore.CYAN + "[+] Time interval to change IP (seconds) [default=60]: ") or 60)
    change_count = int(input(Fore.CYAN + "[+] Number of times to change IP [0 for infinite]: ") or 0)

    os.system("cls" if get_os() == 'windows' else "clear")
    print(Box.Lines("Onyx-Development"))
    print(Fore.GREEN + "Ensure your SOCKS proxy is set to 127.0.0.1:9050\n")

    # IP Change Logic
    try:
        if change_count == 0:
            while True:
                change_ip()
                time.sleep(time_interval)
        else:
            for _ in range(change_count):
                change_ip()
                time.sleep(time_interval)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Process interrupted by user. Exiting...")
    finally:
        stop_tor()
        print(Fore.YELLOW + "[+] TOR service stopped.")

# Entry point
if __name__ == '__main__':
    main()
