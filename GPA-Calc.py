import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Grade Calculator")

# Initialize session state to track subject count and data
if "subject_count" not in st.session_state:
    st.session_state.subject_count = 1
if "subjects" not in st.session_state:
    st.session_state.subjects = []

# Add Subject Button
if st.button("➕ Add Another Subject"):
    st.session_state.subject_count += 1

# Collect subject info
st.markdown("### Enter Subject Grades and Weights")
subjects = []
for i in range(st.session_state.subject_count):
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        name = st.text_input(f"Subject {i+1} Name", key=f"name_{i}")
    with col2:
        grade = st.slider(f"Grade {i+1} (0.0–4.0)", 0.0, 4.0, 3.0, 0.1, key=f"grade_{i}")
    with col3:
        weight = st.number_input(f"Credit {i+1}", min_value=0.0, key=f"weight_{i}")
    
    subjects.append({"name": name, "grade": grade, "weight": weight})

# Calculate GPA Button
if st.button("🎓 Calculate GPA"):
    total_weight = sum(s["weight"] for s in subjects if s["name"])
    total_score = sum(s["grade"] * s["weight"] for s in subjects if s["name"])
    
    if total_weight > 0:
        gpa = total_score / total_weight
        st.success(f"Your GPA is: **{gpa:.2f}**")
    else:
        st.error("Please enter valid credits for each subject.")

# Optional: Display summary table
if subjects:
    st.markdown("### 📋 Subject Summary")
    st.dataframe(subjects)
# Plotting
fig, ax = plt.subplots()
x = range(st.session_state.subject_count)
ax.bar(x, gpa, color='skyblue')
ax.set_xticks(x)
ax.set_xticklabels([f"Assignment {i+1}" for i in x])
ax.set_xlabel("Assignments")
ax.set_ylabel("Scores")
ax.set_title("Scores per Assignment")
st.pyplot(fig)


