import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Page config:
st.set_page_config(
    page_title="Shaped AI, Home",
    page_icon=r"Anka (7).png",
    layout="centered"
)

# Hide all unneeded parts of streamlit (keep your existing hiding code here)
# ...

# Centered header image
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("shaped-ai.png", use_column_width=True)

# Introduction section
st.header("Welcome to Your Free AI Math Instructor 🤖", anchor=False)
st.write("""
Our AI-powered math tutor combines cutting-edge technology with curriculum-aligned learning to help you master mathematics. 
Whether you're preparing for competitions or academic exams, get personalized guidance and adaptive practice problems.
""")

# Performance graph section
st.header("Performance Metrics 📊", anchor=False)

# Create sample data
data = {
    "Test": ["AIME 2024", "MATH-500", "CNMO 2024"],
    "Score": [39.2, 90.2, 43.2],
    "Model": ["Shaped-AI", "Shaped-AI", "Shaped-AI"]
}

df = pd.DataFrame(data)

# Create animated bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df['Test'], df['Score'], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])

# Add aesthetic elements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#444')
ax.spines['bottom'].set_color('#444')
ax.tick_params(axis='x', colors='#555')
ax.tick_params(axis='y', colors='#555')
ax.set_facecolor('#fafafa')

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', color='#444')

plt.title("Model Performance Comparison", pad=20, color='#333')
st.pyplot(fig)

# Model comparison section
st.subheader("Benchmark Comparison", anchor=False)
st.write("""
- AIME 2024 (Pass@1): 39.2%
- MATH-500 (EM): 90.2%
- CNMO 2024 (Pass@1): 43.2%
""")

# Create columns for model comparison
col4, col5 = st.columns(2)
with col4:
    st.metric("Astra AI", "84.6%", "Composite Score")
    
with col5:
    st.metric("Shaped-AI", "91.3%", "Composite Score")

st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
st.metric("ChatGPT-4o", "78.9%", "Composite Score")

# Add some spacing
st.markdown("<div style='height: 50px'></div>", unsafe_allow_html=True)
