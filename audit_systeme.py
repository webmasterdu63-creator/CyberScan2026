import subprocess
import platform
import socket
import os

def get_kernel():
    return platform.release()

def get_modules():
    return subprocess.getoutput("lsmod")

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

def get_services():
    return subprocess.getoutput("systemctl --type=service --state=running")

def outdated_packages():
    return subprocess.getoutput("apt list --upgradable 2>/dev/null")

def dangerous_permissions():
    return subprocess.getoutput("find / -perm -4000 2>/dev/null")

def sudo_users():
    return subprocess.getoutput("getent group sudo")

def suspicious_processes():
    return subprocess.getoutput("ps aux | grep -E 'nc|netcat|nmap|hydra|john'")

def open_ports():
    result = subprocess.getoutput("ss -tuln")
    return result

def audit_systeme():
    print("===========================================")
    print("      CyberScan2026 — Audit Système")
    print("===========================================\n")

    print("Kernel :", get_kernel(), "\n")

    print("Firewall :")
    print(get_firewall(), "\n")

    print("Audit SSH :")
    sshd, config = audit_ssh()
    print("SSH :", sshd)
    print(config, "\n")

    print("Services actifs :")
    print(get_services(), "\n")

    print("Paquets obsolètes :")
    print(outdated_packages(), "\n")

    print("Permissions dangereuses (SUID) :")
    print(dangerous_permissions(), "\n")

    print("Utilisateurs sudo :")
    print(sudo_users(), "\n")

    print("Processus suspects :")
    print(suspicious_processes(), "\n")

    print("Ports ouverts :")
    print(open_ports(), "\n")

    print("Audit système terminé.")
