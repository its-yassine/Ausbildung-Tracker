# Ausbildung Application Tracker (Bewerbungs-Tracker)
<img width="1737" height="882" alt="image" src="https://github.com/user-attachments/assets/af7f4c79-2642-4d62-bda9-e459c5670998" />


A lightweight web application built with **Python**, **SQLite**, and **Streamlit** to organize and track *Ausbildung* applications for **Fachinformatiker für Anwendungsentwicklung** in Germany.

## Features

- **Add Applications:** Log company details, target city, specialization, application status, date, and custom notes.
- **Live Overview Metrics:** Uses SQL `GROUP BY` aggregations to calculate total applications, submitted applications, interviews, and offers in real time.
- **City Filtering:** Filter logged companies by target city.
- **Status Management:** Update application progress (`Planned`, `Applied`, `Interview`, `Offer`, `Rejected`) or delete outdated entries.
- **Local SQLite Storage:** Zero external database setup required—data persists locally in `applications.db`.

## Tech Stack

- **Language:** Python 3
- **Frontend / UI:** Streamlit
- **Database:** SQLite (`sqlite3`)

## Project Structure

```text
ausbildung-tracker/
├── app.py              # Streamlit user interface and interaction logic
├── database.py         # SQLite database initialization and CRUD queries
├── requirements.txt    # Python package dependencies
├── .gitignore          # Excludes local database and virtual environment files
└── README.md           # Project documentation
```

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/its-yassine/ausbildung-tracker.git
   cd ausbildung-tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

---

## Projektübersicht (Deutsch)

Eine schlanke Webanwendung auf Basis von **Python**, **SQLite** und **Streamlit** zur strukturierten Verwaltung von Bewerbungen für eine Ausbildung zum **Fachinformatiker für Anwendungsentwicklung**.

- **Funktionen:** Bewerbungen erfassen, Status aktualisieren, nach Städten filtern und Kennzahlen über SQL-Abfragen (`GROUP BY`) auswerten.
- **Ziel:** Praktische Umsetzung von Grundlagen in Python, relationalen Datenbanken (SQL) und Versionskontrolle mit Git/GitHub.
