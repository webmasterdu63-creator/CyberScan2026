import socket
import subprocess
import platform

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def check_firewall():
    try:
        ufw = subprocess.getoutput("ufw status")
        if "active" in ufw:
            return "UFW actif"
    except:
        pass

    try:
        nft = subprocess.getoutput("nft list ruleset")
        if "table" in nft:
            return "nftables actif"
    except:
        pass

    try:
        ipt = subprocess.getoutput("iptables -L")
        if "Chain" in ipt:
            return "iptables actif"
    except:
        pass

    return "Aucun firewall actif"

def scan_rapide():
    print("===========================================")
    print("      CyberScan2026 — Scan Rapide")
    print("===========================================\n")

    # IP locale
    ip = subprocess.getoutput("hostname -I").split()[0]
    print(f"Adresse IP locale : {ip}")

    # Ports essentiels
    ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL"
    }

    print("\nScan des ports essentiels :")
    for port, name in ports.items():
        status = "OUVERT" if scan_port(ip, port) else "fermé"
        print(f" - Port {port} ({name}) : {status}")

    # SSH
    ssh_status = subprocess.getoutput("systemctl is-active ssh")
    print(f"\nService SSH : {ssh_status}")

    # Firewall
    fw = check_firewall()
    print(f"Firewall : {fw}")

    # Kernel
    kernel = platform.release()
    print(f"Version du kernel : {kernel}")

    print("\nScan rapide terminé.")
