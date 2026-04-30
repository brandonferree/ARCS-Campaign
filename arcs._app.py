import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ARCS Campaign Logger", layout="wide")
st.title("🌌 ARCS CAMPAIGN LOGGER")
st.markdown("### Fill exactly like the **Campaign Log** sheet")

# Header
col1, col2 = st.columns([1, 3])
with col1:
    date = st.date_input("Date", datetime.today())
with col2:
    vod = st.text_input("VOD Link", placeholder="https://... or HOME/IRL")

num_players = st.slider("Number of Players", 1, 4, 4)

fates = [
    "Steward", "Founder", "Magnate", "Advocate", "Caretaker", "Partisan", "Admiral",
    "Believer", "Pathfinder", "Planet Breaker", "Hegemon", "Pirate", "Blight Speaker",
    "Pacifist", "Peacekeeper", "Warden", "Overlord", "Survivalist", "Redeemer",
    "Guardian", "Naturalist", "Gate Wraith", "Conspirator", "Judge"
]

player_options = ["Brandon", "Mark", "Rachael", "Arthur", "James", "Michael"]

players = []

st.subheader("Campaign Input")

for i in range(num_players):
    st.markdown(f"### Player {i+1}")
    row_cols = st.columns([1, 2, 3, 1, 1, 3, 1, 1, 3, 1])  # Mimics Excel column spacing

    with row_cols[0]:
        st.write("**Name**")
        name = st.selectbox("Name", player_options, key=f"name_{i}", index=i, label_visibility="collapsed")

    # Act I
    with row_cols[1]:
        st.write("**Act I Fate**")
        fate1 = st.selectbox("Fate", fates, key=f"f1_{i}", index=4, label_visibility="collapsed")
    with row_cols[2]:
        success1 = st.checkbox("Success?", value=True, key=f"s1_{i}")
    with row_cols[3]:
        score1 = st.number_input("Score", min_value=0, value=5, key=f"sc1_{i}", label_visibility="collapsed")

    # Act II
    with row_cols[4]:
        st.write("**Act II Fate**")
        fate2 = st.selectbox("Fate", fates, key=f"f2_{i}", index=13, label_visibility="collapsed")
    with row_cols[5]:
        success2 = st.checkbox("Success?", value=True, key=f"s2_{i}")
    with row_cols[6]:
        score2 = st.number_input("Score", min_value=0, value=10, key=f"sc2_{i}", label_visibility="collapsed")

    # Act III
    with row_cols[7]:
        st.write("**Act III Fate**")
        fate3 = st.selectbox("Fate", fates, key=f"f3_{i}", index=21, label_visibility="collapsed")
    with row_cols[8]:
        victory3 = st.checkbox("Victory?", value=True, key=f"v3_{i}")
    with row_cols[9]:
        score3 = st.number_input("Score", min_value=0, value=70, key=f"sc3_{i}", label_visibility="collapsed")

    players.append({
        "name": name,
        "fate1": fate1, "success1": success1, "score1": score1,
        "fate2": fate2, "success2": success2, "score2": score2,
        "fate3": fate3, "victory3": victory3, "score3": score3
    })

    st.divider()

# Generate Button
if st.button("🚀 Generate Paste Block for Campaign Log", type="primary", use_container_width=True):
    paste = f"Date\t{date}\tVOD Link\t{vod}\n"
    paste += "Act I\t\t\t\t\tAct II\t\t\t\t\tAct III\n"

    for p in players:
        paste += f"{p['name']}\t{p['fate1']}\t{p['success1']}\t{p['score1']}\t\t"
        paste += f"{p['name']}\t{p['fate2']}\t{p['success2']}\t{p['score2']}\t\t"
        paste += f"{p['name']}\t{p['fate3']}\t{p['victory3']}\t{p['score3']}\n"

    st.success("✅ Ready to paste!")
    st.code(paste, language="text")
    st.balloons()

st.caption("Copy the block above and paste it into your **Campaign Log** sheet → Refresh Excel")
