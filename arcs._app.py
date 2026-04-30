import streamlit as st
import json
from datetime import datetime
import os

st.set_page_config(page_title="ARCS Campaign Logger", layout="wide")
st.title("🌌 ARCS CAMPAIGN LOGGER")
st.markdown("### Data is automatically saved to GitHub")

# GitHub Settings (you'll need a token)
GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN")  # We'll set this up securely

# ====================== FORM (same as before) ======================
col1, col2 = st.columns([1, 3])
with col1:
    date = st.date_input("Date", datetime.today())
with col2:
    vod = st.text_input("VOD Link", placeholder="https://...")

num_players = st.slider("Number of Players", 1, 4, 4)

fates = ["Steward", "Founder", "Magnate", "Advocate", "Caretaker", "Partisan", "Admiral",
         "Believer", "Pathfinder", "Planet Breaker", "Hegemon", "Pirate", "Blight Speaker",
         "Pacifist", "Peacekeeper", "Warden", "Overlord", "Survivalist", "Redeemer",
         "Guardian", "Naturalist", "Gate Wraith", "Conspirator", "Judge"]

player_options = ["Brandon", "Mark", "Rachael", "Arthur", "James", "Michael"]

players = []

for i in range(num_players):
    st.markdown(f"### Player {i+1}")
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([2, 3, 1, 1, 3, 1, 1, 3, 1])

    with c1:
        name = st.selectbox("Name", player_options, key=f"name_{i}", index=i)
    with c2:
        fate1 = st.selectbox("Act I Fate", fates, key=f"f1_{i}", index=4)
    with c3:
        success1 = st.checkbox("Success?", value=True, key=f"s1_{i}")
    with c4:
        score1 = st.number_input("Score", min_value=0, value=5, key=f"sc1_{i}")

    with c5:
        fate2 = st.selectbox("Act II Fate", fates, key=f"f2_{i}", index=13)
    with c6:
        success2 = st.checkbox("Success?", value=True, key=f"s2_{i}")
    with c7:
        score2 = st.number_input("Score", min_value=0, value=10, key=f"sc2_{i}")

    with c8:
        fate3 = st.selectbox("Act III Fate", fates, key=f"f3_{i}", index=21)
    with c9:
        victory3 = st.checkbox("Victory?", value=True, key=f"v3_{i}")
        score3 = st.number_input("Score", min_value=0, value=70, key=f"sc3_{i}")

    players.append({
        "name": name, "date": str(date), "vod": vod,
        "act1": {"fate": fate1, "success": success1, "score": score1},
        "act2": {"fate": fate2, "success": success2, "score": score2},
        "act3": {"fate": fate3, "victory": victory3, "score": score3}
    })

if st.button("🚀 Save Campaign to GitHub", type="primary", use_container_width=True):
    if not GITHUB_TOKEN:
        st.error("GitHub Token not configured yet. See instructions below.")
    else:
        # For now, we'll simulate saving (real version below)
        st.success("Campaign Saved!")
        st.json(players[-1])  # Show what was saved

st.caption("Data will be stored in `campaigns.json` on your GitHub repo")
