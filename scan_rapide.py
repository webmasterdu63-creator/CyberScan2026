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
    output = []
    output.append("=== Scan Rapide ===")

    print("===========================================")
    print("      CyberScan2026 — Scan Rapide")
    print("===========================================\n")

    # IP locale
    ip = subprocess.getoutput("hostname -I").split()[0]
    line = f"Adresse IP locale : {ip}"
    print(line)
    output.append(line)

    # Ports essentiels
    ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL"
    }

    print("\nScan des ports essentiels :")
    output.append("\nScan des ports essentiels :")

    for port, name in ports.items():
        status = "OUVERT" if scan_port(ip, port) else "fermé"
        line = f" - Port {port} ({name}) : {status}"
        print(line)
        output.append(line)

    # SSH
    ssh_status = subprocess.getoutput("systemctl is-active ssh")
    line = f"\nService SSH : {ssh_status}"
    print(line)
    output.append(line)

    # Firewall
    fw = check_firewall()
    line = f"Firewall : {fw}"
    print(line)
    output.append(line)

    # Kernel
    kernel = platform.release()
    line = f"Version du kernel : {kernel}"
    print(line)
    output.append(line)

    print("\nScan rapide terminé.")
    output.append("\nScan rapide terminé.")

    return "\n".join(output)
