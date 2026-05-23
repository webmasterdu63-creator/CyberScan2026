from scan_rapide import scan_rapide
from scan_complet import scan_complet

def menu():
    while True:
        print("\n===========================================")
        print("        CyberScan2026 — Menu Principal")
        print("===========================================\n")
        print("1 - Scan rapide")
        print("2 - Scan complet")
        print("3 - Audit système (bientôt)")
        print("4 - Scan réseau local (bientôt)")
        print("5 - Générer un rapport HTML (bientôt)")
        print("0 - Quitter\n")

        choix = input("Votre choix : ")

        if choix == "1":
            scan_rapide()
        elif choix == "2":
            scan_complet()
        elif choix == "0":
            print("Fermeture de CyberScan2026.")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()
