import subprocess
import socket
import re

def get_local_ip():
    ip = subprocess.getoutput("hostname -I").split()[0]
    return ip

def get_subnet(ip):
    parts = ip.split(".")
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"

def scan_arp():
    return subprocess.getoutput("arp -a")

def parse_arp_output(arp_output):
    devices = []
    lines = arp_output.split("\n")
    for line in lines:
        match = re.search(r"\((.*?)\) at ([0-9a-f:]{17})", line)
        if match:
            ip = match.group(1)
            mac = match.group(2)
            devices.append((ip, mac))
    return devices

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def scan_reseau():
    print("===========================================")
    print("      CyberScan2026 — Scan Réseau Local")
    print("===========================================\n")

    ip = get_local_ip()
    subnet = get_subnet(ip)

    print(f"Adresse IP locale : {ip}")
    print(f"Sous-réseau détecté : {subnet}\n")

    print("Scan ARP en cours...")
    arp_output = scan_arp()
    devices = parse_arp_output(arp_output)

    if not devices:
        print("Aucun appareil détecté.")
        return

    print(f"\nAppareils détectés ({len(devices)}) :\n")

    for ip, mac in devices:
        print(f"IP : {ip} | MAC : {mac}")

        print("  Ports ouverts :")
        for port in [22, 80, 443]:
            status = "OUVERT" if scan_port(ip, port) else "fermé"
            print(f"   - Port {port} : {status}")

        print()

    print("Scan réseau terminé.")
