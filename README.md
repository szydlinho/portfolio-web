# Portfolio — Paweł Szydlik

Jednostronicowa strona wizytówkowa (PL/EN): o mnie, umiejętności, projekty, kontakt.

**Live:** https://szydlinho.github.io/portfolio-web/

## Stack

- [Flask](https://flask.palletsprojects.com/) — treść i routing (PL `/`, EN `/en/`)
- [Frozen-Flask](https://frozen-flask.readthedocs.io/) — zamraża stronę do statycznego HTML/CSS/JS
- GitHub Actions + GitHub Pages — automatyczny build i deploy przy każdym pushu na `main`

## Struktura

```
.
├── app.py                    # treść strony (PROFILE, SKILLS, PROJECTS) + trasy Flask
├── freeze.py                 # generuje statyczną wersję do build/
├── templates/
│   ├── base.html             # layout: head, header, stopka
│   └── index.html            # sekcje: hero, o mnie, umiejętności, projekty, kontakt
├── static/
│   ├── css/style.css
│   └── js/main.js
└── .github/workflows/deploy.yml
```

## Rozwój lokalny

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5000
```

Podgląd statycznej wersji (tej, którą widzi produkcja):

```bash
python freeze.py
cd build && python -m http.server 8000
```

## Edycja treści

Cała treść (imię, opis, umiejętności, projekty, linki) znajduje się w słownikach
`PROFILE`, `SKILLS` i `PROJECTS` na górze `app.py` — nie trzeba ruszać HTML/CSS,
żeby zaktualizować tekst. Push na `main` automatycznie przebudowuje i publikuje stronę.

## Deploy

Push na `main` uruchamia `.github/workflows/deploy.yml`: instaluje zależności,
zamraża stronę (`freeze.py`) i publikuje `build/` na branchu `gh-pages`, z którego
serwuje ją GitHub Pages (**Settings → Pages** → branch `gh-pages`, `/root`).

Opcjonalna własna domena: odkomentować i uzupełnić `cname:` w `deploy.yml`, wpisać
domenę w **Settings → Pages → Custom domain**.
