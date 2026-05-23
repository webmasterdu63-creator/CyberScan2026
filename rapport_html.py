import datetime

def generer_rapport_html(scan_rapide_data, scan_complet_data, audit_data, reseau_data):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Rapport CyberScan2026</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #0d1117;
                color: #e6edf3;
                padding: 20px;
            }}
            h1, h2 {{
                color: #58a6ff;
            }}
            .section {{
                background: #161b22;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 8px;
                border: 1px solid #30363d;
            }}
            pre {{
                background: #0d1117;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
                border: 1px solid #30363d;
            }}
        </style>
    </head>
    <body>

        <h1>Rapport CyberScan2026</h1>
        <p>Généré le : {date}</p>

        <div class="section">
            <h2>Scan Rapide</h2>
            <pre>{scan_rapide_data}</pre>
        </div>

        <div class="section">
            <h2>Scan Complet</h2>
            <pre>{scan_complet_data}</pre>
        </div>

        <div class="section">
            <h2>Audit Système</h2>
            <pre>{audit_data}</pre>
        </div>

        <div class="section">
            <h2>Scan Réseau Local</h2>
            <pre>{reseau_data}</pre>
        </div>

        <h2 style="color:#3fb950;">Rapport généré avec CyberScan2026 — TechNews365</h2>

    </body>
    </html>
    """

    with open("rapport.html", "w") as f:
        f.write(html)

    print("Rapport HTML généré : rapport.html")
