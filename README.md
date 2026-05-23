<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.12-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Security-CyberScan2026-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge">
</p>

CyberScan2026

CyberScan 2026 est un assistant de cybersécurité conçu pour aider les administrateurs système et webmasters à détecter rapidement les failles de configuration les plus courantes : ports ouverts, absence de firewall, mauvaise configuration SSH, services exposés, etc.

L’objectif est simple : fournir un outil léger, rapide et compréhensible, capable d’identifier les erreurs basiques qui ouvrent la porte aux attaques modernes (DDoS, scans automatisés, brute-force, botnets).

---

## 🚀 Fonctionnalités (MVP)

- Analyse des ports locaux les plus sensibles (22, 80, 443, 3306…)
- Détection de la présence d’un firewall (UFW, nftables, iptables)
- Analyse de la configuration SSH (root login, password auth…)
- Rapport clair et lisible dans le terminal
- Score de sécurité global sur 100

---

## 🛠️ Technologies

- Python 3.x
- Modules standards (socket, subprocess, pathlib)
- Optionnel : `rich` pour un affichage amélioré

---

## 📊 Roadmap

### Version 1.0 — MVP
- Scan ports locaux
- Détection firewall
- Analyse SSH
- Score de sécurité

### Version 2.0 — Avancée
- Analyse HTTP/HTTPS
- Détection CMS vulnérables
- Analyse TLS/SSL
- Export PDF du rapport

### Version 3.0 — Pro
- Interface graphique (PyQt6)
- Version Docker
- Version serveur (API REST)
- Intégration dans TechNews365 OS Admin

---

## 📝 Licence

Projet sous licence MIT — libre d’utilisation, modification et distribution.

---

## 👤 Auteur

Projet créé par Jean (TechNews365), 2026.
Qu’est‑ce que CyberScan2026 ?

CyberScan2026 est un outil d’analyse de sécurité pour Linux.
Il permet de :

    analyser les ports ouverts

    vérifier le firewall

    analyser le système

    scanner le réseau local

    générer un rapport HTML complet

🟦 1. Installation
✔️ Prérequis

    Linux (Ubuntu, Mint, TechNews365 OS…)

    Python 3 installé

✔️ Télécharger CyberScan2026

Dans un terminal :
Code

git clone https://github.com/webmasterdu63-creator/CyberScan2026
cd CyberScan2026

🟩 2. Lancer CyberScan2026

Dans le dossier du programme :
Code

python3 main.py

Tu verras le menu :
Code

1 - Scan rapide
2 - Scan complet
3 - Audit système
4 - Scan réseau local
5 - Générer un rapport HTML
0 - Quitter

🟦 3. Fonctionnement des scans
1 — Scan rapide

Analyse les ports essentiels + firewall + SSH + kernel.
2 — Scan complet

Analyse profonde du système :

    ports 1 à 65535

    services

    firewall

    SSH

    permissions dangereuses

    paquets obsolètes

    réseau local

3 — Audit système

Analyse de configuration :

    kernel

    firewall

    SSH

    services

    SUID

    sudoers

4 — Scan réseau local

Liste les appareils connectés :

    IP

    MAC

    ports ouverts (22, 80, 443)

5 — Rapport HTML

Génère un fichier :
Code

rapport.html

Avec :

    scan rapide

    scan complet

    audit système

    scan réseau

    score de sécurité

🟨 4. Où trouver le rapport HTML ?

Dans le dossier CyberScan2026 :
Code

rapport.html

Tu peux l’ouvrir avec :

    Firefox

    Chrome

    Edge

    Opera GX



---

## 📦 Installation (à venir)

Le projet sera installable via :

