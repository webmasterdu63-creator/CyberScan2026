from scan_rapide import scan_rapide
from scan_complet import scan_complet
from audit_systeme import audit_systeme
from scan_reseau import scan_reseau
from rapport_html import generer_rapport_html

def menu():
    while True:
        print("\n===========================================")
        print("        CyberScan2026 — Menu Principal")
        print("===========================================\n")
        print("1 - Scan rapide")
        print("2 - Scan complet")
        print("3 - Audit système")
        print("4 - Scan réseau local")
        print("5 - Générer un rapport HTML")
        print("0 - Quitter\n")

        choix = input("Votre choix : ")

        if choix == "1":
            scan_rapide()

        elif choix == "2":
            scan_complet()

        elif choix == "3":
            audit_systeme()

        elif choix == "4":
            scan_reseau()

        elif choix == "5":
            # Version simple : texte placeholder
            scan_rapide_data = "Résultats du scan rapide."
            scan_complet_data = "Résultats du scan complet."
            audit_data = "Résultats de l'audit système."
            reseau_data = "Résultats du scan réseau."

            generer_rapport_html(scan_rapide_data, scan_complet_data, audit_data, reseau_data)

        elif choix == "0":
            print("Fermeture de CyberScan2026.")
            break

        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()
