import socket
import subprocess
import platform
import os

def scan_tcp_ports(ip):
    open_ports = []
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        try:
            s.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports

def scan_udp_ports(ip, ports=[53, 67, 68, 123, 161]):
    open_udp = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.5)
            sock.sendto(b"", (ip, port))
            sock.recvfrom(1024)
            open_udp.append(port)
        except:
            pass
    return open_udp

def get_services():
    return subprocess.getoutput("systemctl --type=service --state=running")

def get_firewall():
    fw = subprocess.getoutput("ufw status")
    if "active" in fw:
        return "UFW actif"

    nft = subprocess.getoutput("nft list ruleset")
    if "table" in nft:
        return "nftables actif"

    ipt = subprocess.getoutput("iptables -L")
    if "Chain" in ipt:
        return "iptables actif"

    return "Aucun firewall actif"

def audit_ssh():
    sshd = subprocess.getoutput("systemctl is-active ssh")
    config = subprocess.getoutput("grep -E 'PermitRootLogin|PasswordAuthentication' /etc/ssh/sshd_config")
    return sshd, config

def kernel_info():
    return platform.release(), subprocess.getoutput("lsmod")

def outdated_packages():
    return subprocess.getoutput("apt list --upgradable 2>/dev/null")

def dangerous_permissions():
    return subprocess.getoutput("find / -perm -4000 2>/dev/null")

def scan_local_network():
    return subprocess.getoutput("arp -a")

def suspicious_processes():
    return subprocess.getoutput("ps aux | grep -E 'nc|netcat|nmap|hydra|john'")

def sudo_users():
    return subprocess.getoutput("getent group sudo")

def scan_complet():
    print("===========================================")
    print("      CyberScan2026 — Scan Complet")
    print("===========================================\n")

    ip = subprocess.getoutput("hostname -I").split()[0]
    print(f"Adresse IP locale : {ip}\n")

    print("Scan des ports TCP (1–65535)...")
    tcp = scan_tcp_ports(ip)
    print(f"Ports TCP ouverts : {tcp}\n")

    print("Scan des ports UDP essentiels...")
    udp = scan_udp_ports(ip)
    print(f"Ports UDP ouverts : {udp}\n")

    print("Services actifs :")
    print(get_services(), "\n")

    print("Firewall :")
    print(get_firewall(), "\n")

    print("Audit SSH :")
    sshd, config = audit_ssh()
    print(f"SSH : {sshd}")
    print(config, "\n")

    print("Kernel :")
    kernel, modules = kernel_info()
    print(f"Version : {kernel}\n")

    print("Paquets obsolètes :")
    print(outdated_packages(), "\n")

    print("Permissions dangereuses (SUID) :")
    print(dangerous_permissions(), "\n")

    print("Réseau local :")
    print(scan_local_network(), "\n")

    print("Processus suspects :")
    print(suspicious_processes(), "\n")

    print("Utilisateurs sudo :")
    print(sudo_users(), "\n")

    print("Scan complet terminé.")
