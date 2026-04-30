import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ARCS Campaign Logger", layout="wide", initial_sidebar_state="expanded")
st.title("🌌 ARCS CAMPAIGN LOGGER")
st.markdown("### Log your campaign in the exact 3-Act format")

# ====================== HEADER ======================
col_date, col_vod = st.columns([1, 3])
with col_date:
    date = st.date_input("Date", datetime.today())
with col_vod:
    vod = st.text_input("VOD Link", placeholder="https://... or HOME/IRL")

num_players = st.slider("Number of Players", 1, 4, 4)

# Fates list (from your spreadsheet)
fates = [
    "Steward", "Founder", "Magnate", "Advocate", "Caretaker", "Partisan", "Admiral",
    "Believer", "Pathfinder", "Planet Breaker", "Hegemon", "Pirate", "Blight Speaker",
    "Pacifist", "Peacekeeper", "Warden", "Overlord", "Survivalist", "Redeemer",
    "Guardian", "Naturalist", "Gate Wraith", "Conspirator", "Judge"
]

player_options = ["Brandon", "Mark", "Rachael", "Arthur", "James", "Michael"]

# ====================== THREE ACT PANELS ======================
act_cols = st.columns(3)

players = []

for i in range(num_players):
    # ACT I (contains the Name field)
    with act_cols[0]:
        if i == 0:
            st.markdown("### **Act I** 🛡️")
        with st.container(border=True):
            st.markdown(f"**Player {i+1}**")
            name = st.selectbox("Name", player_options, key=f"name_{i}", index=i)
            fate1 = st.selectbox("Fate", fates, key=f"fate1_{i}", index=4)   # Caretaker
            success1 = st.checkbox("Success?", value=True, key=f"succ1_{i}")
            score1 = st.number_input("Score", min_value=0, value=5, key=f"score1_{i}")

    # ACT II
    with act_cols[1]:
        if i == 0:
            st.markdown("### **Act II** 🌌")
        with st.container(border=True):
            st.markdown(f"**Player {i+1}** — {name}")   # Shows the name from Act I
            fate2 = st.selectbox("Fate", fates, key=f"fate2_{i}", index=13)
            success2 = st.checkbox("Success?", value=True, key=f"succ2_{i}")
            score2 = st.number_input("Score", min_value=0, value=10, key=f"score2_{i}")

    # ACT III
    with act_cols[2]:
        if i == 0:
            st.markdown("### **Act III** ☄️")
        with st.container(border=True):
            st.markdown(f"**Player {i+1}** — {name}")
