"""
P-SCAN - Python Port Scanner
Author: Sam
Description: Multi-mode port scanner with CLI and interactive support
"""

import socket
import threading
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

#----------------- Ports ----------------------

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    161: "SNMP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

# ----------- ARGUMENT PARSING -----------
def parse_args():
    parser = argparse.ArgumentParser(description="P-SCAN Port Scanner By Sam")
    parser.add_argument("target", nargs="?", help="Target IP address")
    parser.add_argument("-s", action="store_true", help="Standard Scan, Ports 1–1024")
    parser.add_argument("-f", action="store_true", help="Full Scan, Ports 1–65535")
    parser.add_argument("-c", nargs=2, type=int, metavar=("START", "END"), help="Custom Port Range")
    parser.add_argument("-sm", action="store_true", help="Stealth Mode (slow, low detection)")
    parser.add_argument("--ghost", action="store_true", help="Ghost Mode (ultra quiet, minimal probing)")
    parser.add_argument("-v", action="store_true", help="Verbose Mode")
    
    return parser.parse_args()  # This MUST be at the very end

#---------------- BANNER ---------------------------

def print_banner():
    banner = f"""{Fore.GREEN}
██████╗      ███████╗╔██████╗╔═█████╗███╗   ██╗
██╔══██      ██╔════╝██╔════╝██╔══██║████╗  ██║
██████╝      ███████╗██║     ███████║██╔██╗ ██║
██╔══╝ ████╗ ╚════██║██║     ██╔══██║██║╚██╗██║
██║    ╚═══╝ ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝          ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
           P - S C A N
           By - Sam{
Style.RESET_ALL}"""
    print(banner)

# ----------------- OS DETECTION ----------------------

def detect_os(banner):
    b = banner.lower()
    if "windows" in b:
        return "Windows"
    if "ubuntu" in b or "debian" in b:
        return "Linux"
    if "freebsd" in b:
        return "FreeBSD"
    if "darwin" in b or "macos" in b:
        return "macOS"
    return "Unknown"

# ----------------- PROBING ---------------------------

def probe_service(sock, port, target):
    try:
        if port in (80, 8080, 8000):
            sock.sendall(
                b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
            )
        elif port == 25:
            sock.sendall(b"HELO test\r\n")
    except:
        pass

# ----------------- SCANNER ---------------------------

def scan_port(target, port, timeout, open_ports, verbose):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        if sock.connect_ex((target, port)) != 0:
            sock.close()
            return

        banner = ""
        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except:
            pass

        if not banner:
            probe_service(sock, port, target)
            try:
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                pass

        service = COMMON_PORTS.get(port, "Unknown service")
        os_guess = detect_os(banner)

        open_ports.append((port, service, banner, os_guess))

        print(f"{Fore.GREEN}[OPEN] Port {port}{Style.RESET_ALL}")
        if verbose:
            print(f"  Service : {service}")
            print(f"  Banner  : {banner if banner else 'No response'}")
            print(f"  OS Guess: {os_guess}")

        sock.close()

    except:
        pass

# --------------- SCAN TYPE MENU (INTERACTIVE MODE) ----------------

def choose_scan_type():
    print("\nSelect scan type:")
    print("1) Standard Scan (1 - 1024)")
    print("2) Full Scan (1 - 65535)")
    print("3) Custom Scan")

    choice = input("\nEnter option (1/2/3): ").strip()

    if choice == "1":
        return 1, 1024
    elif choice == "2":
        return 1, 65535
    elif choice == "3":
        try:
            start = int(input("Enter start port: "))
            end = int(input("Enter end port: "))
            if start < 1 or end > 65535 or start > end:
                raise ValueError
            return start, end
        except ValueError:
            print("Invalid range. Using standard scan.")
            return 1, 1024
    else:
        print("Invalid option. Using standard scan.")
        return 1, 1024

# ----------------- OS SUMMARY ------------------------

def summarize_os(open_ports):
    os_count = {}
    for _, _, _, os_guess in open_ports:
        if os_guess != "Unknown":
            os_count[os_guess] = os_count.get(os_guess, 0) + 1
    return max(os_count, key=os_count.get) if os_count else "Unknown"

def choose_scan_mode():
    print("\nSelect scan mode:")
    print("0) Standard")
    print("1) Verbose")
    print("2) Stealth")
    print("3) Ghost")

    choice = input("\nEnter option (0-3): ").strip()

    verbose = False
    stealth = False
    ghost = False

    if choice == "1":
        verbose = True
    elif choice == "2":
        stealth = True
    elif choice == "3":
        ghost = True
    elif choice == "0":
        pass
    else:
        print("Invalid option. Defaulting to Standard mode.")

    return verbose, stealth, ghost

# ----------------- MAIN ------------------------------

def main():
    args = parse_args()
    print_banner()

    # ---- MODE DECISION ----
    if args.target:
        target = args.target
        verbose = args.v
        target = args.target
        stealth = args.stealth
        ghost = args.ghost

         # Check for stealth mode or ghost mode
        if args.sm:
            timeout = 2.0  # Slower scan for stealth
            print(f"{Fore.YELLOW}[STEALTH MODE] Using slower scan...{Style.RESET_ALL}")
        elif args.ghost:
            timeout = 5.0  # Ultra slow for ghost mode
            print(f"{Fore.CYAN}[GHOST MODE] Ultra quiet scan...{Style.RESET_ALL}")
        else:
            timeout = 0.5  # Normal speed

        if args.f:
            start_port, end_port = 1, 65535
        elif args.s:
            start_port, end_port = 1, 1024
        elif args.c:
            start_port, end_port = args.c
        else:
            start_port, end_port = 1, 1024
    else:
    # INTERACTIVE MODE
        target = input("Enter target IP address: ").strip()
    if not target:
        print("No IP address provided.")
        return

    verbose, stealth, ghost = choose_scan_mode()
    start_port, end_port = choose_scan_type()

    if stealth:
        timeout = 2.0
        print(f"{Fore.YELLOW}[STEALTH MODE] Using slower scan...{Style.RESET_ALL}")
    elif ghost:
        timeout = 5.0
        print(f"{Fore.CYAN}[GHOST MODE] Ultra quiet scan...{Style.RESET_ALL}")
    else:
        timeout = 0.5


    print(f"\nScanning {target}")
    print(f"Ports: {start_port} - {end_port}\n")

    open_ports = []
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(
            target=scan_port,
            args=(target, port, timeout, open_ports, verbose)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan complete.")

    if open_ports:
        print("\nOpen ports found:\n")
        for port, service, banner, os_guess in open_ports:
            print(f"Port {port}")
            print(f"  Service : {service}")
            print(f"  Banner  : {banner if banner else 'No response'}")
            print(f"  OS Guess: {os_guess}\n")
        print(f"Most likely OS: {summarize_os(open_ports)}")
    else:
        print("No open ports found.")

# ----------------- ENTRY -----------------------------

if __name__ == "__main__":
    main()

