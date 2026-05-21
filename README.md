# cyberScan2026

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

## 📦 Installation (à venir)

Le projet sera installable via :

