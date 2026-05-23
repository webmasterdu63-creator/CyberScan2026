<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.12-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Security-CyberScan2026-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge">
</p>

# CyberScan2026  
Outil d’analyse de sécurité pour Linux — par TechNews365

CyberScan2026 est un scanner de sécurité complet permettant d’analyser :
- les ports ouverts
- le firewall
- les services critiques
- la configuration SSH
- les permissions dangereuses
- les appareils du réseau local
- et de générer un rapport HTML complet

---

## 🚀 Installation

### 1. Installer Python 3
CyberScan2026 fonctionne avec Python 3.

Vérifier :

python3 --version
Code


### 2. Télécharger CyberScan2026

git clone https://github.com/webmasterdu63-creator/CyberScan2026
cd CyberScan2026
Code


---

## ▶️ Lancer CyberScan2026

Dans le dossier du projet :

python3 main.py
Code


Vous verrez le menu :

1 - Scan rapide
2 - Scan complet
3 - Audit système
4 - Scan réseau local
5 - Générer un rapport HTML
0 - Quitter
Code


---

## 🧪 Fonctionnalités

### 🔹 1. Scan rapide
Analyse :
- ports essentiels (22, 80, 443…)
- firewall (UFW / nftables / iptables)
- SSH
- kernel

### 🔹 2. Scan complet
Analyse avancée :
- ports 1 à 65535
- services actifs
- permissions SUID
- paquets obsolètes
- configuration SSH
- firewall
- réseau local

### 🔹 3. Audit système
Vérifie :
- kernel
- firewall
- SSH
- services
- sudoers
- permissions dangereuses

### 🔹 4. Scan réseau local
Détecte :
- IP des appareils
- adresses MAC
- ports ouverts (22, 80, 443)

### 🔹 5. Rapport HTML
Génère un fichier :

rapport.html
Code

Avec :
- scan rapide
- scan complet
- audit système
- scan réseau
- score de sécurité

---

## 📄 Rapport HTML

Le rapport est généré automatiquement dans le dossier du projet :

rapport.html
Code


Il peut être ouvert avec :
- Firefox
- Chrome
- Edge
- Opera GX

---

## 🛠️ Dépendances

Aucune installation externe n’est nécessaire.  
CyberScan2026 utilise uniquement :
- Python 3
- socket
- subprocess
- platform

---

## 👤 Auteur
Développé par **Jean — TechNews365 OS**

---

## 📌 Licence
Projet open‑source — libre d’utilisation et de modification.
