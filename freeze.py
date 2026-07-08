"""
Zamraża stronę Flask do statycznych plików HTML/CSS/JS w folderze build/.
Uruchamiane lokalnie (`python freeze.py`) albo automatycznie przez
GitHub Actions przy każdym `git push` na branch main.
"""
from flask_frozen import Freezer
from app import app

app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_RELATIVE_URLS"] = False  # ścieżki od / — wymaga własnej domeny na roocie

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    print("Gotowe — statyczne pliki w folderze build/")
