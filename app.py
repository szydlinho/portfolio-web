from flask import Flask, render_template, url_for

app = Flask(__name__)

PROFILE = {
    "name": "Paweł Szydlik",
    "email": "pszydlik@gmail.com", 
    "linkedin": "https://pl.linkedin.com/in/pawel-szydlik-52baba146",
    "github": "https://github.com/szydlinho/", 
    "role": {
        "pl": "Analiza danych / Python & R & SQL",
        "en": "Data analysis / Python & R & SQL",
    },
    "tagline": {
        "pl": (
            "Buduję narzędzia do pracy z danymi — od zapytań SQL, "
            "przez analizy w R, po gotowe aplikacje w Pythonie."
        ),
        "en": (
            "I build tools for working with data — from SQL queries, "
            "through analysis in R, to finished applications in Python."
        ),
    },
    "bio": {
        "pl": (
            "Analityk danych z dowświadczeniem. Zajmuję się "
            "analizą danych, automatyzacją i budową aplikacji — od surowych "
            "danych po gotowe narzędzie, z którego można realnie korzystać."
        ),
        "en": (
            "Experienced data analyst. I work on "
            "data analysis, automation and application development — turning raw data "
            "into a tool people can actually use."
        ),
    },
    "location": {"pl": "Polska", "en": "Poland"},
}

SKILLS = [
    {
        "name": "Python",
        "note": {
            "pl": "pandas, Djano, automatyzacja, skrypty, API",
            "en": "pandas, Django, automation, scripting, API",
        },
    },
    {
        "name": "R",
        "note": {
            "pl": "analiza statystyczna, wizualizacja danych, uczenie maszynowe",
            "en": "statistical analysis, data visualization, machine learning",
        },
    },
    {
        "name": "SQL",
        "note": {
            "pl": "projektowanie i optymalizacja zapytań, funkcje analityczne, agregacje",
            "en": "query design and optimization, analytical functions, aggregations",
        },
    },
]

# id — dwucyfrowy numer wiersza; url/tags wspólne dla obu wersji językowych
PROJECTS = [
    {
        "id": "01",
        "url": "https://monitorportfela.pl",  # TODO: link do aplikacji
        "tags": ["Python", "Flask", "SQL"],
        "name": {
            "pl": "Aplikacja do zarządzania portfelem",
            "en": "Portfolio management app",
        },
        "desc": {
            "pl": "Narzędzie do śledzenia i analizy inwestycji.",
            "en": "A tool for tracking and analysing investments.",
        },
    },
    {
        "id": "02",
        "url": "#",  # TODO: link do bloga
        "tags": ["Python", "R"],
        "name": {"pl": "Hobby Blog", "en": "Passion Blog"},
        "desc": {
            "pl": "Notatki o danych, kodzie i analizie w piłce nożnej.",
            "en": "Notes on data, code and analysis in football.",
        },
    },
]

UI = {
    "pl": {
        "nav_about": "o mnie",
        "nav_skills": "umiejętności",
        "nav_projects": "projekty",
        "nav_contact": "kontakt",
        "cta_projects": "zobacz projekty",
        "cta_contact": "napisz do mnie",
        "eyebrow_whoami": "$ whoami",
        "eyebrow_about": "# o mnie",
        "eyebrow_skills": "# umiejętności",
        "eyebrow_projects": "-- projekty",
        "eyebrow_contact": "# kontakt",
        "table_id": "id",
        "table_project": "projekt",
        "table_stack": "stack",
        "label_email": "email",
        "label_linkedin": "linkedin",
        "label_github": "github",
    },
    "en": {
        "nav_about": "about",
        "nav_skills": "skills",
        "nav_projects": "projects",
        "nav_contact": "contact",
        "cta_projects": "view projects",
        "cta_contact": "get in touch",
        "eyebrow_whoami": "$ whoami",
        "eyebrow_about": "# about",
        "eyebrow_skills": "# skills",
        "eyebrow_projects": "-- projects",
        "eyebrow_contact": "# contact",
        "table_id": "id",
        "table_project": "project",
        "table_stack": "stack",
        "label_email": "email",
        "label_linkedin": "linkedin",
        "label_github": "github",
    },
}


def render_page(lang: str):
    other_lang = "en" if lang == "pl" else "pl"
    other_endpoint = "index_en" if lang == "pl" else "index_pl"

    profile = {
        "name": PROFILE["name"],
        "email": PROFILE["email"],
        "linkedin": PROFILE["linkedin"],
        "github": PROFILE["github"],
        "role": PROFILE["role"][lang],
        "tagline": PROFILE["tagline"][lang],
        "bio": PROFILE["bio"][lang],
        "location": PROFILE["location"][lang],
    }
    skills = [{"name": s["name"], "note": s["note"][lang]} for s in SKILLS]
    projects = [
        {
            "id": p["id"],
            "url": p["url"],
            "tags": p["tags"],
            "name": p["name"][lang],
            "desc": p["desc"][lang],
        }
        for p in PROJECTS
    ]

    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        projects=projects,
        ui=UI[lang],
        lang=lang,
        other_lang=other_lang,
        other_endpoint=other_endpoint,
    )


@app.route("/")
def index_pl():
    return render_page("pl")


@app.route("/en/")
def index_en():
    return render_page("en")


if __name__ == "__main__":
    app.run(debug=True)
