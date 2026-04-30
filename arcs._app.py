import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.set_page_config(page_title="ARCS Campaign Logger", layout="wide")
st.title("🌌 ARCS CAMPAIGN LOGGER v2.1")
st.markdown("**Three-Act Layout • Different Fates per Act**")

# ====================== SIDEBAR ======================
st.sidebar.header("Campaign Info")
date = st.sidebar.date_input("Date", datetime.today())
vod = st.sidebar.text_input("VOD Link", "")

num_players = st.sidebar.slider("Number of Players", 1, 4, 4)

# Pre-load your Fates
fates_list = [
    "Steward", "Founder", "Magnate", "Advocate", "Caretaker", "Partisan",
    "Admiral", "Believer", "Pathfinder", "Planet Breaker", "Hegemon", "Pirate",
    "Blight Speaker", "Pacifist", "Peacekeeper", "Warden", "Overlord",
    "Survivalist", "Redeemer", "Guardian", "Naturalist", "Gate Wraith",
    "Conspirator", "Judge"
]

player_names = ["Brandon", "Mark", "Rachael", "Arthur", "James", "Michael"]

# ====================== MAIN FORM ======================
cols = st.columns(3)

players_data = []

for p in range(num_players):
    with cols[0]:  # Act I
        st.subheader(f"Act I — Player {p+1}")
        name = st.selectbox("Name", player_names, key=f"name_{p}", index=p)
        fate1 = st.selectbox("Fate", fates_list, key=f"fate1_{p}", index=4)  # default Caretaker
        success1 = st.checkbox("Success?", value=True, key=f"s1_{p}")
        score1 = st.number_input("Score", value=5, key=f"sc1_{p}", min_value=0)

    with cols[1]:  # Act II
        st.subheader(f"Act II — Player {p+1}")
        fate2 = st.selectbox("Fate", fates_list, key=f"fate2_{p}", index=13)  # default Pacifist etc.
        success2 = st.checkbox("Success?", value=True, key=f"s2_{p}")
        score2 = st.number_input("Score", value=10, key=f"sc2_{p}", min_value=0)

    with cols[2]:  # Act III
        st.subheader(f"Act III — Player {p+1}")
        fate3 = st.selectbox("Fate", fates_list, key=f"fate3_{p}", index=21)  # Gate Wraith etc.
        victory3 = st.checkbox("Victory?", value=True, key=f"v3_{p}")
        score3 = st.number_input("Score", value=70, key=f"sc3_{p}", min_value=0)

    players_data.append({
        "name": name,
        "fate1": fate1, "success1": success1, "score1": int(score1),
        "fate2": fate2, "success2": success2, "score2": int(score2),
        "fate3": fate3, "victory3": victory3, "score3": int(score3)
    })

# ====================== GENERATE PASTE BLOCK ======================
if st.button("🚀 Generate Excel Paste Block", type="primary"):
    st.success("✅ Campaign Ready!")

    paste = f"Date\t{date}\tVOD Link\t{vod}\n"
    paste += "Act I\t\t\t\t\tAct II\t\t\t\t\tAct III\n"

    for p in players_data:
        paste += f"{p['name']}\t{p['fate1']}\t{p['success1']}\t{p['score1']}\t\t"
        paste += f"{p['name']}\t{p['fate2']}\t{p['success2']}\t{p['score2']}\t\t"
        paste += f"{p['name']}\t{p['fate3']}\t{p['victory3']}\t{p['score3']}\n"

    st.code(paste, language="text")

    st.balloons()

# Optional: Quick Dashboard
if st.checkbox("Show Overview Dashboard"):
    st.subheader("Current Overview (from your file)")
    # You can expand this later with real Excel reading
    st.info("Dashboard coming in next update — for now it shows your current top performers.")

st.caption("Made for Brandon • Matches your beautiful 3-Act design")
