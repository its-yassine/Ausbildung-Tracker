import streamlit as st
from datetime import date
import database as db

# Page setup
st.set_page_config(page_title="Ausbildung Tracker", layout="wide")
db.init_db()

st.title("Ausbildung Application Tracker")
st.caption("Fachinformatiker für Anwendungsentwicklung — Bewerbungsübersicht")

STATUS_OPTIONS = ["Planned", "Applied", "Interview", "Offer", "Rejected"]

# --- TOP METRICS (SQL GROUP BY) ---
counts = db.get_status_counts()
total = sum(counts.values())

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Applications", total)
col2.metric("Applied", counts.get("Applied", 0))
col3.metric("Interviews", counts.get("Interview", 0))
col4.metric("Offers", counts.get("Offer", 0))

st.divider()

# --- SIDEBAR: ADD NEW APPLICATION ---
with st.sidebar:
    st.header("Add Application")
    with st.form("new_app_form", clear_on_submit=True):
        company = st.text_input("Company Name *")
        city = st.selectbox("City", ["Berlin", "Hamburg", "Leipzig", "Munich", "Other"])
        role = st.text_input("Specialization", value="Fachinformatiker Anwendungsentwicklung")
        status = st.selectbox("Status", STATUS_OPTIONS)
        date_applied = st.date_input("Date Applied", value=date.today())
        notes = st.text_area("Notes (e.g., German level required, contact person)")
        
        submitted = st.form_submit_button("Save Application")
        if submitted:
            if company.strip():
                db.add_application(
                    company.strip(), 
                    city, 
                    role.strip(), 
                    status, 
                    str(date_applied), 
                    notes.strip()
                )
                st.success(f"Added {company}!")
                st.rerun()
            else:
                st.error("Company name is required.")

# --- MAIN AREA: VIEW & MANAGE APPLICATIONS ---
applications = db.get_all_applications()

if not applications:
    st.info("No applications logged yet. Use the sidebar on the left to add your first company.")
else:
    # Filter by city
    cities = ["All"] + sorted(list(set(app["city"] for app in applications)))
    selected_city = st.selectbox("Filter by City", cities)
    
    filtered_apps = [
        app for app in applications 
        if selected_city == "All" or app["city"] == selected_city
    ]

    st.subheader(f"Applications ({len(filtered_apps)})")
    st.dataframe(filtered_apps, use_container_width=True, hide_index=True)

    # Quick Update / Delete Section
    st.subheader("Update or Remove Entry")
    app_choices = {f"{app['id']} - {app['company']} ({app['city']})": app for app in filtered_apps}
    selected_label = st.selectbox("Select an application", list(app_choices.keys()))
    selected_app = app_choices[selected_label]

    u_col1, u_col2, u_col3 = st.columns([2, 1, 1])
    with u_col1:
        new_status = st.selectbox(
            "Change Status", 
            STATUS_OPTIONS, 
            index=STATUS_OPTIONS.index(selected_app["status"])
        )
    with u_col2:
        st.write("")
        st.write("")
        if st.button("Update Status", use_container_width=True):
            db.update_status(selected_app["id"], new_status)
            st.success("Updated!")
            st.rerun()
    with u_col3:
        st.write("")
        st.write("")
        if st.button("Delete Entry", type="secondary", use_container_width=True):
            db.delete_application(selected_app["id"])
            st.warning("Deleted.")
            st.rerun()
