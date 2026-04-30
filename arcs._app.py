import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import io

st.set_page_config(page_title="ARCS Campaign Logger", layout="wide")
st.title("🌌 ARCS CAMPAIGN LOGGER")
st.markdown("**Input new campaigns • Auto-generate Excel paste block • Live Overview Dashboard**")

# ====================== SIDEBAR ======================
st.sidebar.header("Campaign Info")
date = st.sidebar.date_input("Campaign Date", datetime.today())
vod = st.sidebar.text_input("VOD Link (optional)", "")

num_players = st.sidebar.slider("Number of Players", 1, 4, 3)

# ====================== MAIN FORM ======================
st.header("Player Data")

players = []
for i in range(num_players):
    with st.expander(f"Player {i+1}", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(f"Name", key=f"name_{i}", value=["Brandon", "Mark", "Rachael", "Arthur"][i] if i < 4 else "")
            fate = st.text_input(f"Fate", key=f"fate_{i}", value="Caretaker")
        with col2:
            st.subheader("Act I")
            a1_success = st.checkbox("Success", value=True, key=f"a1s_{i}")
            a1_score = st.number_input("Score", value=5, key=f"a1score_{i}")

            st.subheader("Act II")
            a2_success = st.checkbox("Success", value=True, key=f"a2s_{i}")
            a2_score = st.number_input("Score", value=11, key=f"a2score_{i}")

            st.subheader("Act III")
            a3_victory = st.checkbox("Victory", value=True, key=f"a3v_{i}")
            a3_score = st.number_input("Score", value=74, key=f"a3score_{i}")

        players.append({
            "name": name, "fate": fate,
            "a1_success": a1_success, "a1_score": int(a1_score),
            "a2_success": a2_success, "a2_score": int(a2_score),
            "a3_victory": a3_victory, "a3_score": int(a3_score)
        })

# ====================== SUBMIT ======================
if st.button("🚀 Generate Excel Paste Block + Dashboard", type="primary"):
    st.success("Campaign Logged!")

    # === PASTE BLOCK ===
    st.subheader("📋 Copy & Paste this directly into **Campaign Log** sheet")
    paste_block = f"Date\t{date}\tVOD Link\t{vod}\n"
    paste_block += "Act I\t\t\t\t\tAct II\t\t\t\t\tAct III\n"

    for p in players:
        paste_block += f"{p['name']}\t{p['fate']}\t{p['a1_success']}\t{p['a1_score']}\t\t"
        paste_block += f"{p['name']}\t{p['fate']}\t{p['a2_success']}\t{p['a2_score']}\t\t"
        paste_block += f"{p['name']}\t{p['fate']}\t{p['a3_victory']}\t{p['a3_score']}\n"

    st.code(paste_block, language="text")

    # ====================== LIVE DASHBOARD ======================
    st.subheader("📊 Live Overview Dashboard")

    # Current known totals (you can expand this later)
    player_names = ["Brandon", "Mark", "Rachael", "Arthur", "James", "Michael"]
    totals = [63, 48, -10, 3, 3, 0]

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.barplot(x=player_names, y=totals, palette="plasma", ax=ax1)
        ax1.set_title("Lifetime Accumulated Points")
        ax1.tick_params(axis='x', rotation=45)
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        act3_scores = [74, 57, 12]
        act3_names = ["Brandon\n(Caretaker)", "Mark\n(Pathfinder)", "Arthur\n(Gate Wraith)"]
        sns.barplot(x=act3_names, y=act3_scores, palette="viridis", ax=ax2)
        ax2.set_title("Top Act III Scores")
        st.pyplot(fig2)

    # Fate Heatmap
    st.subheader("Fate Plays by Player")
    fate_matrix = pd.DataFrame({
        "Caretaker": [2,0,0,0,0,0],
        "Founder":   [2,0,1,0,1,1],
        "Magnate":   [0,1,0,0,0,0],
        "Advocate":  [1,0,0,0,0,0],
        "Partisan":  [0,0,0,1,0,0],
        "Pacifist":  [0,0,1,0,0,0],
        "Pathfinder":[0,1,1,0,0,0],
        "Gate Wraith":[0,0,0,1,0,0]
    }, index=player_names)

    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.heatmap(fate_matrix, annot=True, fmt="d", cmap="YlGnBu", ax=ax3)
    ax3.set_title("Fate Usage Heatmap")
    st.pyplot(fig3)

    st.balloons()

st.caption("Built for Brandon • Your Arcs empire grows stronger with every campaign")
