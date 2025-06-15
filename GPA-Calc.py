import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("📘 Grade Calculator (4.0 GPA Scale)")

# Initialize session state
if "subject_count" not in st.session_state:
    st.session_state.subject_count = 1

st.markdown("### 📥 Enter Subject Grades and Credits")

# Collect inputs
subjects = []
for i in range(st.session_state.subject_count):
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        name = st.text_input(f"Subject {i+1} Name", key=f"name_{i}")
    with col2:
        grade = st.slider(f"Grade {i+1} (0.0–4.0)", 0.0, 4.0, 3.0, 0.1, key=f"grade_{i}")
    with col3:
        weight = st.slider(f"Credit {i+1}", min_value=0.0, max_value=10.0, value=3.0, step=0.5, key=f"weight_{i}")
    
    if name:
        subjects.append({"name": name, "grade": grade, "weight": weight})

# ✅ Button now BELOW inputs
if st.button("➕ Add Another Subject", key="add_subject"):
    st.session_state.subject_count += 1

# GPA Calculation Button
if st.button("🎓 Calculate GPA", key="calc_gpa"):
    if subjects:
        total_weight = sum(s["weight"] for s in subjects)
        total_score = sum(s["grade"] * s["weight"] for s in subjects)
        if total_weight > 0:
            gpa = total_score / total_weight
            st.success(f"✅ Your GPA is: **{gpa:.2f}**")
        else:
            st.error("⚠️ Total credit cannot be zero.")
    else:
        st.warning("⚠️ Please enter at least one subject.")

# Show Table
if subjects:
    st.markdown("### 📋 Subject Summary")
    st.dataframe(pd.DataFrame(subjects))

    # Plotting
    st.markdown("### 📊 Grades by Subject")
    fig, ax = plt.subplots()
    names = [s["name"] for s in subjects]
    grades = [s["grade"] for s in subjects]
    ax.bar(names, grades, color='skyblue')
    ax.set_ylabel("Grade (0–4.0)")
    ax.set_title("Grades per Subject")
    st.pyplot(fig)
