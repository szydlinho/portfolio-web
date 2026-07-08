# Strona portfolio — Flask

Prosta, jednostronicowa strona wizytówkowa: o Tobie, umiejętności, projekty z linkami, kontakt.

## Uruchomienie lokalnie

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Strona wystartuje na `http://127.0.0.1:5000`.

## Edycja treści

Cała treść strony (imię, opis, umiejętności, projekty, linki, e-mail) znajduje się
na górze pliku **`app.py`**, w słownikach `PROFILE`, `SKILLS` i `PROJECTS`.
Nie trzeba ruszać HTML ani CSS, żeby zaktualizować tekst — wystarczy podmienić
wartości w tych strukturach, np.:

```python
PROJECTS = [
    {
        "id": "01",
        "name": "Nazwa projektu",
        "desc": "Krótki opis.",
        "tags": ["Python", "SQL"],
        "url": "https://link-do-projektu.pl",
    },
    ...
]
```

Pola oznaczone `# TODO` w `app.py` (e-mail, GitHub, linki do projektów) czekają
na Twoje dane.

## Struktura projektu

```
portfolio/
├── app.py                  # treść strony + trasa Flask
├── requirements.txt
├── templates/
│   ├── base.html           # układ strony, nagłówek, stopka
│   └── index.html          # sekcje: hero, o mnie, umiejętności, projekty, kontakt
└── static/
    ├── css/style.css       # cały wygląd
    └── js/main.js          # jedna drobna funkcja (rok w stopce)
```

## Podgląd statycznej wersji lokalnie

Strona nie potrzebuje działającego serwera Flask na produkcji — jest w pełni
statyczna (brak formularzy, logowania, bazy danych). `freeze.py` generuje
gotowe pliki HTML do folderu `build/`:

```bash
python freeze.py
```

Podejrzysz wynik, otwierając `build/index.html` w przeglądarce, albo
serwując go lokalnie:

```bash
cd build && python -m http.server 8000
```

## Wdrożenie na GitHub Pages (darmowy hosting)

### 1. Załóż repozytorium na GitHubie

```bash
cd portfolio
git init
git add .
git commit -m "Pierwsza wersja strony"
git branch -M main
git remote add origin https://github.com/TWOJ-LOGIN/TWOJE-REPO.git
git push -u origin main
```

### 2. Włącz GitHub Pages

Po pierwszym pushu automatycznie odpali się workflow z `.github/workflows/deploy.yml`:
zamraża stronę i publikuje ją na branchu `gh-pages`. Sprawdzisz to w zakładce
**Actions** w repo.

Następnie w repo: **Settings → Pages** → w polu "Source" wybierz branch
`gh-pages`, folder `/ (root)` → Save.

Po chwili strona będzie dostępna pod `https://TWOJ-LOGIN.github.io/TWOJE-REPO/`.

### 3. Podepnij własną domenę (opcjonalnie, ale polecane)

1. Kup domenę `.pl` (np. home.pl, OVH, nazwa.pl) — koszt ok. 50–90 zł/rok.
2. W panelu DNS swojej domeny dodaj:
   - rekordy **A** dla domeny głównej (`twojadomena.pl`), wskazujące na adresy
     GitHub Pages: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
     `185.199.111.153`
   - albo rekord **CNAME** dla `www.twojadomena.pl` → `TWOJ-LOGIN.github.io`
3. W `.github/workflows/deploy.yml` odkomentuj i uzupełnij linię `cname:`
   swoją domeną — GitHub Pages doda wtedy automatycznie plik `CNAME` przy
   każdym wdrożeniu.
4. W **Settings → Pages** wpisz domenę w polu "Custom domain" i zaznacz
   "Enforce HTTPS" (certyfikat SSL GitHub ustawi automatycznie, może to
   potrwać do kilku godzin).

### Aktualizacja treści

Edytujesz dane w `app.py` (patrz sekcja "Edycja treści" wyżej), robisz:

```bash
git add .
git commit -m "Aktualizacja treści"
git push
```

— i za chwilę zmiany są już live. Nie musisz ręcznie odpalać `freeze.py`,
robi to za Ciebie GitHub Actions.
